from dataclasses import dataclass

# TODO disallow Any in other files
from typing import Any, Generic, TypeVar

T = TypeVar("T")


@dataclass
class Result(Generic[T]):
    ok: bool
    value: T


# __orig_class__ may be useful when making this function generic
# https://stackoverflow.com/questions/66927793/how-to-use-isinstance-on-a-generic-type-in-python
def is_list_of_dict(list_: list[Any]) -> Result[list[dict[object, object]]]:
    ok = all([isinstance(x, dict) for x in list_])
    return Result(ok, list_ if ok else [])
