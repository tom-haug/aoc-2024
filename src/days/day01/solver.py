from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Day01Solver(Solver[AnswerType]):
    data: list[str]

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.list_a = []
        self.list_b = []

        for line in input:
            num1, num2 = map(int, line.split())
            self.list_a.append(num1)
            self.list_b.append(num2)

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
