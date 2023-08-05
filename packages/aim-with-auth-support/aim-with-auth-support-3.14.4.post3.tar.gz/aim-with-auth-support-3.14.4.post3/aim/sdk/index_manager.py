import time
import click
import tqdm
import logging
import os

from threading import Thread
from multiprocessing.pool import ThreadPool
from psutil import cpu_count
from pathlib import Path
from functools import partial

from typing import Optional, List


from aim.sdk.maintenance_run import MaintenanceRun
from aim.storage.locking import AutoFileLock
from aim.storage.rockscontainer import RocksContainer

logger = logging.getLogger(__name__)


class RepoIndexManager:
    index_manager_pool = {}

    @classmethod
    def get_index_manager(cls, repo_path: str):
        mng = cls.index_manager_pool.get(repo_path, None)
        if mng is None:
            mng = RepoIndexManager(repo_path)
            cls.index_manager_pool[repo_path] = mng
        return mng

    def __init__(self, repo_path: str):
        self.repo_path = repo_path

        repo_path = Path(self.repo_path)
        self.progress_dir = repo_path / 'meta' / 'progress'
        self.progress_dir.mkdir(parents=True, exist_ok=True)

        self.locks_dir = repo_path / 'locks'
        self.locks_dir.mkdir(parents=True, exist_ok=True)

        self._indexing_in_progress = False
        self._reindex_thread: Thread = None

    @property
    def repo_status(self):
        if self._indexing_in_progress is True:
            return 'indexing in progress'
        if self.reindex_needed:
            return 'needs indexing'
        return 'up-to-date'

    @property
    def reindex_needed(self) -> bool:
        progress_dir = os.path.join(self.repo_path, 'meta', 'progress')
        runs_with_progress = os.listdir(progress_dir)
        return len(runs_with_progress) > 0

    def start_indexing_thread(self):
        logger.info(f'Starting indexing thread for repo \'{self.repo_path}\'')
        self._reindex_thread = Thread(target=self._run_forever, daemon=True)
        self._reindex_thread.start()

    def reindex(self):
        stalled_runs = list(self._unindexed_runs())
        in_progress_runs = list(self._in_progress_runs())
        for run_hash in tqdm.tqdm(stalled_runs, desc='Finalizing stalled runs', total=len(stalled_runs)):
            self._run(run_hash).set_finalization_time()

        # run second pass on newly runs which are killed after reindex started
        click.echo('Checking recent runs...')
        new_stalled_runs = [r for r in in_progress_runs if
                            self._run_has_progress_file(r) and not self._is_run_in_progress(r)]
        if len(new_stalled_runs) > 0:
            click.echo('Found new stalled runs.')
            for run_hash in tqdm.tqdm(new_stalled_runs, desc='Finalizing stalled runs', total=len(new_stalled_runs)):
                self._run(run_hash).set_finalization_time()
        else:
            click.echo('No new stalled runs found.')

    def run_flushes_and_compactions(self):
        runs_to_skip = set(self._in_progress_runs())
        meta_dbs_path = os.path.join(self.repo_path, 'meta', 'chunks')
        seq_dbs_path = os.path.join(self.repo_path, 'seqs', 'chunks')
        meta_dbs_names = set(os.listdir(meta_dbs_path)).difference(runs_to_skip)
        seq_dbs_names = set(os.listdir(seq_dbs_path)).difference(runs_to_skip)
        meta_index_container_path = os.path.join(self.repo_path, 'meta', 'index')

        pool = ThreadPool(cpu_count(logical=False))

        def optimize_container(path, extra_options):
            rc = RocksContainer(path, read_only=True, **extra_options)
            rc.optimize_for_read()

        meta_containers = [os.path.join(meta_dbs_path, db) for db in meta_dbs_names]
        for _ in tqdm.tqdm(
                pool.imap_unordered(partial(optimize_container, extra_options={'compaction': True}), meta_containers),
                desc='Optimizing metadata',
                total=len(meta_containers)
        ):
            pass

        optimize_container(meta_index_container_path, extra_options={'compaction': True})

        seq_containers = [os.path.join(seq_dbs_path, db) for db in seq_dbs_names]
        for _ in tqdm.tqdm(
                pool.imap_unordered(partial(optimize_container, extra_options={}), seq_containers),
                desc='Optimizing sequence data',
                total=len(seq_containers)
        ):
            pass

    def _run_forever(self):
        lock_path = self.locks_dir / 'run_index'
        logger.debug(f'Trying to acquire indexing lock for repo \'{self.repo_path}\'...')
        lock = AutoFileLock(lock_path)
        lock.acquire(timeout=-1)  # block till lock can be acquired
        logger.debug('Lock acquired! Running...')
        idle_cycles = 0
        while True:
            self._indexing_in_progress = False
            for run in self._next_unindexed_run():
                logger.info(f'Found un-indexed run {run.hash}. Indexing...')
                self._indexing_in_progress = True
                idle_cycles = 0
                run.set_finalization_time()
                del run
                # sleep for 2 seconds to release index db lock in between and allow
                # potential running jobs to properly finalize and index Run.
                sleep_interval = 2
                time.sleep(sleep_interval)
            if not self._indexing_in_progress:
                idle_cycles += 1
                sleep_interval = 2 * idle_cycles if idle_cycles < 5 else 10
                logger.info(f'No un-indexed runs found. Next check will run in {sleep_interval} seconds. '
                            f'Waiting for un-indexed run...')
                time.sleep(sleep_interval)

    def _run_has_progress_file(self, run_hash: str) -> bool:
        # This method is required to detect the case when Run was finalized after collecting
        # un-indexed runs. Such case may occur since there's a significant interval between collecting
        # runs and actual indexing and Run might be finalized manually during that period.
        run_progress = os.path.join(self.repo_path, 'meta', 'progress', run_hash)
        return os.path.exists(run_progress)

    def _is_run_in_progress(self, run_hash: str) -> bool:
        lock_path = os.path.join(self.repo_path, 'meta', 'locks', run_hash)
        try:
            fl = AutoFileLock(lock_path, timeout=0)
            fl.acquire()
        except TimeoutError:
            return True
        else:
            fl.release()
            return False

    def _unindexed_runs(self) -> List[str]:
        progress_dir = os.path.join(self.repo_path, 'meta', 'progress')
        runs_with_progress = os.listdir(progress_dir)
        run_hashes = sorted(filter(lambda r: not self._is_run_in_progress(r), runs_with_progress),
                            key=lambda r: os.path.getmtime(os.path.join(progress_dir, r)))
        return run_hashes

    def _in_progress_runs(self) -> List[str]:
        progress_dir = os.path.join(self.repo_path, 'meta', 'progress')
        runs_with_progress = os.listdir(progress_dir)
        run_hashes = sorted(filter(lambda r: self._is_run_in_progress(r), runs_with_progress),
                            key=lambda r: os.path.getmtime(os.path.join(progress_dir, r)))
        return run_hashes

    def _run(self, run_hash):
        return MaintenanceRun(run_hash, repo=self.repo_path)

    def _next_unindexed_run(self) -> Optional[MaintenanceRun]:
        for run_hash in self._unindexed_runs():
            if self._run_has_progress_file(run_hash):
                yield self._run(run_hash)
