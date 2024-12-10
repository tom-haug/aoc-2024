from abc import abstractmethod
from src.shared.controller import Solver


AnswerType = int


class Day09Solver(Solver[AnswerType]):
    @abstractmethod
    def initialize(self, file_path: str):
        ...

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
