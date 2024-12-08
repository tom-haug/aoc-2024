from abc import abstractmethod
from collections import namedtuple
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int

Position = namedtuple("Position", ["x", "y"])


class Day08Solver(Solver[AnswerType]):
    map_width: int
    map_height: int

    frequency_location: dict[str, list[Position]]

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.map_width = len(input[0])
        self.map_height = len(input)
        self.frequency_location = {}
        for y, line in enumerate(input):
            for x, char in enumerate(line):
                if char == ".":
                    continue

                if char not in self.frequency_location:
                    self.frequency_location[char] = [Position(x, y)]
                else:
                    self.frequency_location[char].append(Position(x, y))

    def _is_within_bounds(self, position: Position) -> bool:
        return 0 <= position.x < self.map_width and 0 <= position.y < self.map_height

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
