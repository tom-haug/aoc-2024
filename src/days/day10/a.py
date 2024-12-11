from src.shared.controller import Controller
from src.days.day10.solver import AnswerType, Day10Solver
from src.shared.file_result import FileResult


class Day10PartASolver(Day10Solver):
    def solve(self) -> AnswerType:
        return sum(
            len({peak for peak in self._explore(trailhead)})
            for trailhead in self.trailheads
        )


class Day10PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(10, "a")

    def _new_solver(self):
        return Day10PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [
            FileResult("sample01.txt", 2),
            FileResult("sample02.txt", 4),
            FileResult("sample03.txt", 3),
            FileResult("sample04.txt", 36),
        ]


if __name__ == "__main__":
    controller = Day10PartAController()
    controller.run()
