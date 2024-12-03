from typing import Any, Generic, Optional, TypeVar

from attr import dataclass


T = TypeVar("T")


@dataclass
class FileResult(Generic[T]):
    file_path: str
    expected_result: Optional[T]
    extra_params: dict[str, Any] = {}
