from abc import abstractmethod
from typing import NamedTuple, TypeAlias

from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Plot(NamedTuple):
    x: int
    y: int

    def neighbors(self) -> list["Plot"]:
        """Return all adjacent plots."""
        return [
            Plot(self.x, self.y - 1),  # up
            Plot(self.x + 1, self.y),  # right
            Plot(self.x, self.y + 1),  # down
            Plot(self.x - 1, self.y),  # left
        ]


# Type aliases for clarity
Region: TypeAlias = set[Plot]
NamedRegion: TypeAlias = tuple[str, Region]


class Day12Solver(Solver[AnswerType]):
    plots: dict[Plot, str]

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.plots = {}
        for row, line in enumerate(input):
            for col, char in enumerate(line):
                self.plots[Plot(col, row)] = char

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
