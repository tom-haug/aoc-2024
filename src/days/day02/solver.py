from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Day02Solver(Solver[AnswerType]):
    reports: list[list[int]]

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.reports = [[int(char)for char in line.split()] for line in input]

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
