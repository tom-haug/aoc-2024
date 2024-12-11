from src.shared.controller import Controller
from src.days.day10.solver import AnswerType, Day10Solver
from src.shared.file_result import FileResult


class Day10PartBSolver(Day10Solver):
    def solve(self) -> AnswerType:
        return sum(
            len([peak for peak in self._explore(trailhead)])
            for trailhead in self.trailheads
        )


class Day10PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(10, "b")

    def _new_solver(self):
        return Day10PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [
            FileResult("sample05.txt", 3),
            FileResult("sample06.txt", 13),
            FileResult("sample07.txt", 227),
            FileResult("sample04.txt", 81),
        ]


if __name__ == "__main__":
    controller = Day10PartBController()
    controller.run()
