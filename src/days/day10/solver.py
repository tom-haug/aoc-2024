from abc import abstractmethod
from collections import namedtuple
from typing import Generator

import numpy as np
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines
from nptyping import NDArray

AnswerType = int


Position = namedtuple("Position", ["x", "y"])


class Day10Solver(Solver[AnswerType]):
    data: NDArray
    trailheads: list[Position]

    def initialize(self, file_path: str):
        lines = load_text_file_lines(file_path)

        self.data = np.array(
            [[int(char) if char != "." else -1 for char in line] for line in lines]
        )

        self.trailheads = [Position(x, y) for y, x in zip(*np.where(self.data == 0))]

    def _explore(self, position: Position) -> Generator[Position, None, None]:
        if self.data[position.y][position.x] == 9:
            yield position

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for dx, dy in directions:
            new_x, new_y = position.x + dx, position.y + dy

            if (
                0 <= new_y < len(self.data)
                and 0 <= new_x < len(self.data[0])
                and int(self.data[new_y][new_x])
                == int(self.data[position.y][position.x]) + 1
            ):
                yield from self._explore(Position(new_x, new_y))

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
