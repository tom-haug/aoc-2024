from __future__ import annotations
from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines

AnswerType = int


class Equation:
    answer: int
    operands: list[int]

    def __init__(self, answer: int, operands: list[int]):
        self.answer = answer
        self.operands = operands


class Day07Solver(Solver[AnswerType]):
    equations: list[Equation]

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)

        self.equations = []
        for line in input:
            answer, operands_list = line.split(": ")
            operands = [int(operand) for operand in operands_list.split(" ")]
            self.equations.append(Equation(int(answer), operands))

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
