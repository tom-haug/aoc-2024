from __future__ import annotations
from abc import abstractmethod
from enum import Enum
from typing import NamedTuple, TypeAlias

from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3


class Plot(NamedTuple):
    x: int
    y: int

    def neighbors(self) -> list[tuple[Direction, Plot]]:
        """Return all adjacent plots."""
        return [
            (Direction.Up, Plot(self.x, self.y - 1)),
            (Direction.Right, Plot(self.x + 1, self.y)),
            (Direction.Down, Plot(self.x, self.y + 1)),
            (Direction.Left, Plot(self.x - 1, self.y)),
        ]


NamedRegion: TypeAlias = tuple[str, set[Plot]]


class Day12Solver(Solver[AnswerType]):
    plots: dict[Plot, str]

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.plots = {}
        for row, line in enumerate(input):
            for col, char in enumerate(line):
                self.plots[Plot(col, row)] = char

    def _get_regions(self) -> list[NamedRegion]:
        regions: list[NamedRegion] = []
        while self.plots:
            plot, plant_type = next(iter(self.plots.items()))
            region = self._find_touching_plots(plot, plant_type)
            regions.append((plant_type, region))
        return regions

    def _find_touching_plots(self, start: Plot, plant_type: str) -> set[Plot]:
        if start not in self.plots or self.plots[start] != plant_type:
            return set()

        region: set[Plot] = set()
        queue = [start]

        while queue:
            plot = queue.pop(0)
            if plot not in region:
                region.add(plot)
                self.plots.pop(plot)

                queue.extend(
                    neighbor
                    for _, neighbor in plot.neighbors()
                    if (
                        neighbor in self.plots
                        and self.plots[neighbor] == plant_type
                        and neighbor not in region
                    )
                )
        return region

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
