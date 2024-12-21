from src.shared.controller import Controller
from src.days.day15.solver import AnswerType, Day15Solver
from src.shared.file_result import FileResult


class Day15PartASolver(Day15Solver):
    @property
    def x_scale_factor(self) -> int:
        return 1


class Day15PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(15, "a")

    def _new_solver(self):
        return Day15PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 2028), FileResult("sample02.txt", 10092)]


if __name__ == "__main__":
    controller = Day15PartAController()
    controller.run()
