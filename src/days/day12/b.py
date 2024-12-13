from src.shared.controller import Controller
from src.days.day12.solver import AnswerType, Day12Solver
from src.shared.file_result import FileResult


class Day12PartBSolver(Day12Solver):
    def solve(self) -> AnswerType:
        return -1


class Day12PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(12, "b")

    def _new_solver(self):
        return Day12PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", -1)]


if __name__ == "__main__":
    controller = Day12PartBController()
    controller.run()
