from src.shared.controller import Controller
from src.days.day03.solver import AnswerType, Day03Solver
from src.shared.file_result import FileResult
import re


class Day03PartBSolver(Day03Solver):
    def solve(self) -> AnswerType:
        do = list(match.start() for match in re.finditer(r"do\(\)", self.data))
        dont = list(match.start() for match in re.finditer(r"don\'t\(\)", self.data))
        matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", self.data)
        result = 0
        for mult_match in matches:
            max_do = max(
                (do_idx for do_idx in do if do_idx < mult_match.start()), default=-1
            )
            max_dont = max(
                (dont_idx for dont_idx in dont if dont_idx < mult_match.start()),
                default=-2,
            )
            if max_do > max_dont:
                a, b = mult_match.groups()
                result += int(a) * int(b)
        return result


class Day03PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(3, "b")

    def _new_solver(self):
        return Day03PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample02.txt", 48)]


if __name__ == "__main__":
    controller = Day03PartBController()
    controller.run()
