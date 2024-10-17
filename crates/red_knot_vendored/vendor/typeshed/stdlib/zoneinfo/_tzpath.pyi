from _typeshed import StrPath
from collections.abc import Sequence

# Note: Both here and in clear_cache, the types allow the use of `str` where
# a sequence of strings is required. This should be remedied if a solution
# to this typing bug is found: https://github.com/python/typing/issues/256
def reset_tzpath(to: Sequence[StrPath] | None = None) -> None: ...
def find_tzfile(key: str) -> str | None: ...
def available_timezones() -> set[str]: ...

TZPATH: tuple[str, ...]

class InvalidTZPathWarning(RuntimeWarning): ...