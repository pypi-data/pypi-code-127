import asyncio
import collections
import logging
import multiprocessing
import time

from avocado.core.exceptions import TestFailFast
from avocado.core.task.runtime import RuntimeTaskStatus
from avocado.core.teststatus import STATUSES_NOT_OK

LOG = logging.getLogger(__name__)


class TaskStateMachine:
    """Represents all phases that a task can go through its life."""

    def __init__(self, tasks, status_repo):
        self._requested = collections.deque(tasks)
        self._status_repo = status_repo
        self._triaging = []
        self._ready = []
        self._started = []
        self._finished = []
        self._lock = asyncio.Lock()
        self._cache_lock = asyncio.Lock()

    @property
    def requested(self):
        return self._requested

    @property
    def triaging(self):
        return self._triaging

    @property
    def ready(self):
        return self._ready

    @property
    def started(self):
        return self._started

    @property
    def finished(self):
        return self._finished

    @property
    def lock(self):
        return self._lock

    @property
    def cache_lock(self):
        return self._cache_lock

    @property
    async def complete(self):
        async with self._lock:
            pending = any([self._requested, self._triaging, self._ready, self._started])
        return not pending

    async def abort(self, status_reason=None):
        """Abort all non-started tasks.

        This method will move all non-started tasks to finished with a specific
        reason.

        :param status_reason: string reason. Optional.
        """
        await self.abort_queue("requested", status_reason)
        await self.abort_queue("triaging", status_reason)
        await self.abort_queue("ready", status_reason)

    async def abort_queue(self, queue_name, status_reason=None):
        """Abort all tasks inside a specific queue adding a status reason.

        :param queue_name: a string with the queue name.
        :param status_reason: string reason. Optional.
        """
        to_remove = []
        async with self._lock:
            queue = getattr(self, queue_name)
            for _ in range(len(queue)):
                if queue_name == "requested":
                    runtime_task = queue.popleft()
                else:
                    runtime_task = queue.pop(0)
                to_remove.append(runtime_task)

        if to_remove:
            if status_reason:
                LOG.debug(
                    'Aborting queue "%s" by finishing %u tasks: %s',
                    queue_name,
                    len(to_remove),
                    status_reason,
                )
            else:
                LOG.debug(
                    'Aborting queue "%s" by finishing %u tasks',
                    queue_name,
                    len(to_remove),
                )

        for task in to_remove:
            await self.finish_task(task, status_reason)

    async def finish_task(self, runtime_task, status_reason=None):
        """Include a task to the finished queue with a specific reason.

        This method is assuming that you have removed (pop) the task from the
        original queue.

        :param runtime_task: A running task object.
        :param status_reason: string reason. Optional.
        """
        async with self._lock:
            if runtime_task not in self.finished:
                if status_reason:
                    runtime_task.status = status_reason
                    LOG.debug(
                        'Task "%s" finished with status: %s',
                        runtime_task.task.identifier,
                        status_reason,
                    )
                else:
                    LOG.debug('Task "%s" finished', runtime_task.task.identifier)
                self.finished.append(runtime_task)


class Worker:
    def __init__(
        self,
        state_machine,
        spawner,
        max_triaging=None,
        max_running=None,
        task_timeout=None,
        failfast=False,
    ):
        self._state_machine = state_machine
        self._spawner = spawner
        if max_triaging is None:
            max_triaging = multiprocessing.cpu_count()
        self._max_triaging = max_triaging
        if max_running is None:
            max_running = 2 * multiprocessing.cpu_count() - 1
        self._max_running = max_running
        self._task_timeout = task_timeout
        self._failfast = failfast
        LOG.debug("%s has been initialized", self)

    def __repr__(self):
        fmt = '<Worker spawner="{}" max_triaging={} max_running={} task_timeout={}>'
        return fmt.format(
            self._spawner, self._max_triaging, self._max_running, self._task_timeout
        )

    async def bootstrap(self):
        """Reads from requested, moves into triaging."""
        try:
            async with self._state_machine.lock:
                if len(self._state_machine.triaging) < self._max_triaging:
                    runtime_task = self._state_machine.requested.popleft()
                    self._state_machine.triaging.append(runtime_task)
                    LOG.debug(
                        'Task "%s": requested -> triaging', runtime_task.task.identifier
                    )
                else:
                    return
        except IndexError:
            return

    async def triage(self):
        """Reads from triaging, moves into either: ready or finished."""

        try:
            async with self._state_machine.lock:
                runtime_task = self._state_machine.triaging.pop(0)
        except IndexError:
            return

        # a task waiting requirements already checked its requirements
        if runtime_task.status != RuntimeTaskStatus.WAIT_DEPENDENCIES:
            # check for requirements a task may have
            requirements_ok = await self._spawner.check_task_requirements(runtime_task)
            if requirements_ok:
                LOG.debug(
                    'Task "%s": requirements OK (will proceed to check '
                    "dependencies)",
                    runtime_task.task.identifier,
                )
            else:
                await self._state_machine.finish_task(
                    runtime_task, RuntimeTaskStatus.FAIL_TRIAGE
                )
                return

        # handle task dependencies
        if runtime_task.dependencies:
            # check of all the dependency tasks finished
            if not runtime_task.are_dependencies_finished():
                async with self._state_machine.lock:
                    self._state_machine.triaging.append(runtime_task)
                    runtime_task.status = RuntimeTaskStatus.WAIT_DEPENDENCIES
                await asyncio.sleep(0.1)
                return

            # dependencies finished, let's check if they finished
            # successfully, so we can move on with the parent task
            dependencies_ok = runtime_task.can_run()
            if not dependencies_ok:
                LOG.debug(
                    'Task "%s" has failed dependencies', runtime_task.task.identifier
                )
                return
        if runtime_task.task.category != "test":
            async with self._state_machine.cache_lock:
                is_task_in_cache = await self._spawner.is_requirement_in_cache(
                    runtime_task
                )
                if is_task_in_cache is None:
                    async with self._state_machine.lock:
                        self._state_machine.triaging.append(runtime_task)
                        runtime_task.status = RuntimeTaskStatus.WAIT
                        await asyncio.sleep(0.1)
                    return

                if is_task_in_cache:
                    await self._state_machine.finish_task(
                        runtime_task, RuntimeTaskStatus.IN_CACHE
                    )
                    runtime_task.result = "pass"
                    return

                await self._spawner.save_requirement_in_cache(runtime_task)

        # the task is ready to run
        async with self._state_machine.lock:
            self._state_machine.ready.append(runtime_task)

    async def start(self):
        """Reads from ready, moves into either: started or finished."""
        try:
            async with self._state_machine.lock:
                runtime_task = self._state_machine.ready.pop(0)
        except IndexError:
            return

        # enforce a rate limit on the number of started (currently
        # running) tasks.  this is a global limit, but the spawners
        # can also be queried with regards to their capacity to handle
        # new tasks
        should_wait = False
        async with self._state_machine.lock:
            if len(self._state_machine.started) >= self._max_running:
                self._state_machine.ready.insert(0, runtime_task)
                runtime_task.status = RuntimeTaskStatus.WAIT
                should_wait = True
        if should_wait:
            await asyncio.sleep(0.1)
            return

        LOG.debug(
            'Task "%s": about to be spawned with "%s"',
            runtime_task.task.identifier,
            self._spawner,
        )
        start_ok = await self._spawner.spawn_task(runtime_task)
        if start_ok:
            LOG.debug('Task "%s": spawned successfully', runtime_task.task.identifier)
            runtime_task.status = RuntimeTaskStatus.STARTED
            if self._task_timeout is not None:
                runtime_task.execution_timeout = time.monotonic() + self._task_timeout
            async with self._state_machine.lock:
                self._state_machine.started.append(runtime_task)
        else:
            await self._state_machine.finish_task(
                runtime_task, RuntimeTaskStatus.FAIL_START
            )

    async def monitor(self):
        """Reads from started, moves into finished."""
        try:
            async with self._state_machine.lock:
                runtime_task = self._state_machine.started.pop(0)
        except IndexError:
            return

        if self._spawner.is_task_alive(runtime_task):
            try:
                if runtime_task.execution_timeout is None:
                    remaining = None
                else:
                    remaining = runtime_task.execution_timeout - time.monotonic()
                await asyncio.wait_for(self._spawner.wait_task(runtime_task), remaining)
            except asyncio.TimeoutError:
                runtime_task.status = RuntimeTaskStatus.TIMEOUT
                await self._spawner.terminate_task(runtime_task)
                message = {
                    "status": "finished",
                    "result": "interrupted",
                    "fail_reason": "Test interrupted: Timeout reached",
                    "time": time.monotonic(),
                    "id": str(runtime_task.task.identifier),
                    "job_id": runtime_task.task.job_id,
                }
                self._state_machine._status_repo.process_message(message)
        # from here, this `task` ran, so, let's check
        # the its latest data in the status repo
        latest_task_data = (
            self._state_machine._status_repo.get_latest_task_data(
                str(runtime_task.task.identifier)
            )
            or {}
        )
        # maybe, the results are not available yet
        while latest_task_data.get("result") is None:
            await asyncio.sleep(0.1)
            latest_task_data = (
                self._state_machine._status_repo.get_latest_task_data(
                    str(runtime_task.task.identifier)
                )
                or {}
            )
        if runtime_task.task.category != "test":
            async with self._state_machine.cache_lock:
                await self._spawner.update_requirement_cache(
                    runtime_task, latest_task_data["result"].upper()
                )
        runtime_task.result = latest_task_data["result"]
        result_stats = set(
            key.upper() for key in self._state_machine._status_repo.result_stats.keys()
        )
        if self._failfast and not result_stats.isdisjoint(STATUSES_NOT_OK):
            await self._state_machine.abort(RuntimeTaskStatus.FAILFAST)
            raise TestFailFast("Interrupting job (failfast).")

        await self._state_machine.finish_task(runtime_task, RuntimeTaskStatus.FINISHED)

    async def run(self):
        """Pushes Tasks forward and makes them do something with their lives."""
        while True:
            is_complete = await self._state_machine.complete
            if is_complete:
                break
            await self.bootstrap()
            await self.triage()
            await self.start()
            await self.monitor()
