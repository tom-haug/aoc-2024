from typing import Any
from src.shared.controller import Controller
from src.days.day14.solver import AnswerType, Day14Solver
from src.shared.file_result import FileResult


class Day14PartBSolver(Day14Solver):
    def solve(self) -> AnswerType:
        # run simulation long enough to find the period where the two partial
        # images are made
        if self.show_visual:
            self._run_simulation(300)

        # equations when the two parital images occur
        # a = 103x - 73
        # b = 101x - 20

        # find the intersection point
        a = 30
        b = 81
        while a != b:
            if a < b:
                a += 103
            else:
                b += 101
        return a


class Day14PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(14, "b")

    def _new_solver(self):
        return Day14PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return []

    def _main_input_extra_params(self) -> dict[str, Any]:
        return {"width": 101, "height": 103}


if __name__ == "__main__":
    controller = Day14PartBController()
    controller.run()
