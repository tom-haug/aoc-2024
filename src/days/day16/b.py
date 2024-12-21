from src.shared.controller import Controller
from src.days.day16.solver import AnswerType, Day16Solver
from src.shared.file_result import FileResult


class Day16PartBSolver(Day16Solver):
    def solve(self) -> AnswerType:
        return -1


class Day16PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(16, 'b')

    def _new_solver(self):
        return Day16PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", -1)]


if __name__ == "__main__":
    controller = Day16PartBController()
    controller.run()
