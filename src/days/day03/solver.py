from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int


class Day03Solver(Solver[AnswerType]):
    data: str

    def initialize(self, file_path: str):
        input = load_text_file(file_path) or ""
        self.data = input

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
