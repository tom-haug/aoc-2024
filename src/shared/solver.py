from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from src.shared.controller import ExtraParams
from src.shared.print_helpers import Colors

_TSolution = TypeVar("_TSolution")


class Solver(ABC, Generic[_TSolution]):
    extra_params: dict[str, Any]

    def initialize_extra_params(self, extra_params: dict[str, Any]):
        self.extra_params = extra_params
        if self.visual_available and not self.show_visual:
            print(
                f"{Colors.WARNING}Visual avaiable, but will not output. Run with --visual flag"
            )

    @property
    def show_visual(self) -> bool:
        return (
            ExtraParams.ShowVisual in self.extra_params
            and self.extra_params[ExtraParams.ShowVisual]
        )

    @property
    def visual_available(self) -> bool:
        return False

    @abstractmethod
    def initialize(self, file_path: str) -> None:
        pass

    @abstractmethod
    def solve(self) -> _TSolution:
        pass
