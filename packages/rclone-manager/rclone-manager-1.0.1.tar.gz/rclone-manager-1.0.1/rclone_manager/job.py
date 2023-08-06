import json
import threading

from . import rclone
from .base import logger

__all__ = ['RCloneJob']


class RCloneJob(rclone.RClone):
    """
    This class is a subclass of the RClone class, and it is used to create a job object that can be used to run a job
    on the cluster. It has a thread that updates the job progress in real time. It also has a callback function that
    is called when the job is finished or terminated.

    :param src: Source path
    :type src: str
    :param dst: Destination path
    :type dst: str
    :param callback: Callback function
    :type callback: callable
    :param args: Flags
    :param kwargs: Options & Config
    """

    def __init__(self, src, dst, callback: callable = None, *args, **kwargs):
        super().__init__(src, dst)
        self.update_frequency = kwargs.pop('update_frequency', '1s')
        self.callback = callback
        self._flags = args + ('verbose', 'use-json-log')
        self._options = {**kwargs, **{'stats': self.update_frequency}}
        self._thread = None
        self._is_finished = False

        self.__task = None

        self._stats = {
            "bytes": 0,
            "checks": 0,
            "deletedDirs": 0,
            "deletes": 0,
            "elapsedTime": 0,
            "errors": 0,
            "eta": None,
            "fatalError": False,
            "renames": 0,
            "retryError": False,
            "speed": 0,
            "totalBytes": 0,
            "totalChecks": 0,
            "totalTransfers": 0,
            "transferTime": 0,
            "transfers": 0
        }

    def run(self, *args, **kwargs):
        """
        Run rclone command.

        :param args: Flags
        :param kwargs: Options & Config (will override the ones passed to the constructor)
        :return: RCloneJob object
        :rtype: RCloneJob
        """
        kwargs.pop('wait', None)  # Job.run() does not support wait
        self.__task = kwargs.pop('task', None)
        logger.info(f"Job {self.name} started")
        super().run(wait=False, *args, **kwargs)
        self._run_thread()
        return self

    def _update_stats(self):
        """
        Update job stats in real time. This function is called by a thread.
        """
        for line in iter(self.process.stdout.readline, ''):
            if line:
                if not line.startswith('{'):
                    continue
                line_json = json.loads(line.rstrip())
                stats = line_json.get('stats', {})
                self._stats.update(stats)
        self._is_finished = True
        if self.__task:
            self.__task.result_handler(self)
        if self.callback:
            self.callback(self)

    def _run_thread(self):
        """
        Run thread that updates job stats in real time. This function is called by the run() function.

        :return: thread object
        :rtype: threading.Thread
        """
        self._thread = threading.Thread(target=self._update_stats, name=self.name + "_thread" + '_stats')
        self._thread.start()
        return self._thread

    def terminate(self):
        """
        Terminate job.
        """
        if self.is_running:
            logger.info(f"Job {self.name} terminated")
            self.process.terminate()
            self._thread.join()
        else:
            logger.info(f"Job {self.name} not running")

    @property
    def stats(self):
        """
        Get job stats.

        :return: Job stats
        :rtype: dict
        """
        return self._stats

    @property
    def is_finished(self):
        """
        Check if job is finished.

        :return: True if job is finished, False otherwise
        :rtype: bool
        """
        return self._is_finished
