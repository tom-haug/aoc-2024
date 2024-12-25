from src.shared.controller import Controller
from src.days.day17.solver import AnswerType, Day17Solver
from src.shared.file_result import FileResult


class Day17PartBSolver(Day17Solver):
    def solve(self) -> AnswerType:
        return ""


class Day17PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(17, "b")

    def _new_solver(self):
        return Day17PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", "")]


if __name__ == "__main__":
    controller = Day17PartBController()
    controller.run()
