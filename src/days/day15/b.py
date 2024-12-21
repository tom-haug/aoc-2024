from src.shared.controller import Controller
from src.days.day15.solver import AnswerType, Day15Solver
from src.shared.file_result import FileResult


class Day15PartBSolver(Day15Solver):
    @property
    def x_scale_factor(self) -> int:
        return 2


class Day15PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(15, "b")

    def _new_solver(self):
        return Day15PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [
            FileResult("sample03.txt", 105 + 207 + 306),
            FileResult("sample02.txt", 9021),
        ]


if __name__ == "__main__":
    controller = Day15PartBController()
    controller.run()
