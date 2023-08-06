from dataclasses import dataclass
from functools import wraps
import logging
import os
import pickle
from typing import Any, ClassVar

logger = logging.getLogger("pickle_function_cache")
OMIT_CACHE = (
    os.getenv("OMIT_PICKLE_FUNCTION_CACHE").strip().lower() in ("1", "true")
) or False


@dataclass(frozen=True)
class ArgsContainer:
    """Represents args and kwargs sent to a function."""

    args: tuple[Any]
    kwargs: tuple[tuple[str, Any]]

    @classmethod
    def from_args_kwargs(cls, *args, **kwargs):
        return cls(
            args=args,
            kwargs=tuple(tuple([a, b]) for a, b in kwargs.items()),
        )


@dataclass
class Cache:
    """
    File that contains pickled cache dict.

    All per-filename instances are tracked in `_filename_caches` for not
    opening the file every time.
    """

    filename: str
    _cache: dict | None = None

    _filename_caches: ClassVar[dict[str, dict]] = {}

    @classmethod
    def load_instance(cls, filename) -> dict:
        """Return info pickled to the file."""
        if os.path.isfile(filename):
            with open(filename, "rb") as fp:
                return dict(pickle.load(fp))
        else:
            with open(filename, "wb") as fp:
                pickle.dump({}, fp)
                return {}

    def get_instance(self) -> dict:
        """Returns the cache."""
        if self._cache is None:
            if self.filename in self._filename_caches:
                self._cache = self._filename_caches[self.filename]
            else:
                self._cache = self.load_instance(self.filename)
                self.sync_global_cache()

        return self._cache

    def save_instance(self) -> None:
        """Saves the cache."""
        self.sync_global_cache()
        with open(self.filename, "wb") as fp:
            pickle.dump(self._cache, file=fp)

    def close_instance(self) -> None:
        """
        Placeholder for code to close the cache if
        cache requires an active file descriptor open.
        """
        pass

    def sync_global_cache(self):
        cache = self.get_instance()
        self._filename_caches[self.filename] = cache

    @classmethod
    def invalidate_cache(cls, filename):
        del cls._filename_caches[filename]
        os.unlink(filename)


if OMIT_CACHE:

    def cache_responses(cache_filename):
        def decor(decorated_func):
            return decorated_func

        return decor

else:

    def cache_responses(cache_filename):
        """Decorate a function with this and the function will get its result cached in a file."""

        def decor(decorated_func):
            @wraps(decorated_func)
            def decorator(*args, **kwargs):
                cache_instance = Cache(filename=cache_filename)
                cache = cache_instance.get_instance()
                logger.debug(cache)
                if decorated_func.__name__ not in cache:
                    cache[decorated_func.__name__] = {}

                arguments = ArgsContainer.from_args_kwargs(*args, **kwargs)
                if arguments in cache[decorated_func.__name__]:
                    logger.debug(
                        f"found result of call to {decorated_func.__name__} with {arguments = }"
                    )
                    result = cache[decorated_func.__name__][arguments]
                    cache_instance.close_instance()
                    return result
                else:
                    logger.debug(f"calling {decorated_func.__name__} with {arguments}")
                    result = decorated_func(*args, **kwargs)
                    if result is None:
                        return

                    cache[decorated_func.__name__][arguments] = result
                    cache_instance.save_instance()
                    return result

            return decorator

        return decor
