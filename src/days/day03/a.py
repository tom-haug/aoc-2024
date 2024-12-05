from src.shared.controller import Controller
from src.days.day03.solver import AnswerType, Day03Solver
from src.shared.file_result import FileResult
import re


class Day03PartASolver(Day03Solver):
    def solve(self) -> AnswerType:
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", self.data)
        result = sum(int(a) * int(b) for a, b in matches)
        return result


class Day03PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(3, "a")

    def _new_solver(self):
        return Day03PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 161)]


if __name__ == "__main__":
    controller = Day03PartAController()
    controller.run()
