from src.shared.controller import Controller
from src.days.day05.solver import AnswerType, Day05Solver
from src.shared.file_result import FileResult


class Day05PartBSolver(Day05Solver):
    def solve(self) -> AnswerType:
        return -1


class Day05PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(5, "b")

    def _new_solver(self):
        return Day05PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", -1)]


if __name__ == "__main__":
    controller = Day05PartBController()
    controller.run()
