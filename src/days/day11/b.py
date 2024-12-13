from src.shared.controller import Controller
from src.days.day11.solver import AnswerType, Day11Solver
from src.shared.file_result import FileResult


class Day11PartBSolver(Day11Solver):
    def solve(self) -> AnswerType:
        return -1


class Day11PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(11, "b")

    def _new_solver(self):
        return Day11PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", -1)]


if __name__ == "__main__":
    controller = Day11PartBController()
    controller.run()
