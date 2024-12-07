from abc import abstractmethod
from collections import namedtuple
from enum import Enum
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3

    def turn_right(self):
        return Direction((self.value + 1) % 4)


Position = namedtuple("Position", ["x", "y"])


def move(position: Position, direction: Direction) -> Position:
    if direction == Direction.Up:
        return Position(position.x, position.y - 1)
    elif direction == Direction.Right:
        return Position(position.x + 1, position.y)
    elif direction == Direction.Down:
        return Position(position.x, position.y + 1)
    else:
        return Position(position.x - 1, position.y)


class Day06Solver(Solver[AnswerType]):
    map_width: int
    map_height: int
    obstructions: set[Position]
    original_guard_position: Position
    original_guard_direction: Direction

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.map_width = len(input[0])
        self.map_height = len(input)
        self.obstructions = set()
        for row_idx, line in enumerate(input):
            for col_idx, char in enumerate(line):
                if char == "#":
                    self.obstructions.add(Position(col_idx, row_idx))
                elif char == "^":
                    self.original_guard_position = Position(col_idx, row_idx)
                    self.original_guard_direction = Direction.Up

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
