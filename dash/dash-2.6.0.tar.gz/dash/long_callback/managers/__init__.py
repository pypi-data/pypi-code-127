from abc import ABC
import inspect
import hashlib


class BaseLongCallbackManager(ABC):
    UNDEFINED = object()

    # Keep a ref to all the ref to register every callback to every manager.
    managers = []

    # Keep every function for late registering.
    functions = []

    def __init__(self, cache_by):
        if cache_by is not None and not isinstance(cache_by, list):
            cache_by = [cache_by]

        self.cache_by = cache_by

        BaseLongCallbackManager.managers.append(self)

        self.func_registry = {}

        # Register all funcs that were added before instantiation.
        # Ensure all celery task are registered.
        for fdetails in self.functions:
            self.register(*fdetails)

    def terminate_job(self, job):
        raise NotImplementedError

    def terminate_unhealthy_job(self, job):
        raise NotImplementedError

    def job_running(self, job):
        raise NotImplementedError

    def make_job_fn(self, fn, progress):
        raise NotImplementedError

    def call_job_fn(self, key, job_fn, args, context):
        raise NotImplementedError

    def get_progress(self, key):
        raise NotImplementedError

    def result_ready(self, key):
        raise NotImplementedError

    def get_result(self, key, job):
        raise NotImplementedError

    def build_cache_key(self, fn, args, cache_args_to_ignore):
        fn_source = inspect.getsource(fn)

        if not isinstance(cache_args_to_ignore, (list, tuple)):
            cache_args_to_ignore = [cache_args_to_ignore]

        if cache_args_to_ignore:
            if isinstance(args, dict):
                args = {k: v for k, v in args.items() if k not in cache_args_to_ignore}
            else:
                args = [
                    arg for i, arg in enumerate(args) if i not in cache_args_to_ignore
                ]

        hash_dict = dict(args=args, fn_source=fn_source)

        if self.cache_by is not None:
            # Caching enabled
            for i, cache_item in enumerate(self.cache_by):
                # Call cache function
                hash_dict[f"cache_key_{i}"] = cache_item()

        return hashlib.sha1(str(hash_dict).encode("utf-8")).hexdigest()

    def register(self, key, fn, progress):
        self.func_registry[key] = self.make_job_fn(fn, progress)

    @staticmethod
    def register_func(fn, progress):
        key = BaseLongCallbackManager.hash_function(fn)
        BaseLongCallbackManager.functions.append(
            (
                key,
                fn,
                progress,
            )
        )

        for manager in BaseLongCallbackManager.managers:
            manager.register(key, fn, progress)

        return key

    @staticmethod
    def _make_progress_key(key):
        return key + "-progress"

    @staticmethod
    def hash_function(fn):
        fn_source = inspect.getsource(fn)
        fn_str = fn_source
        return hashlib.sha1(fn_str.encode("utf-8")).hexdigest()
