import math
from typing import Any
from src.shared.controller import Controller
from src.days.day14.solver import AnswerType, Day14Solver
from src.shared.file_result import FileResult


class Day14PartASolver(Day14Solver):
    def solve(self) -> AnswerType:
        self._run_simulation(100)
        return self.calc_safety_factor()

    def calc_safety_factor(self):
        def in_quadrant(robot, left: bool, top: bool) -> bool:
            return (
                robot.position.x < self.width // 2
                if left
                else robot.position.x > self.width // 2
            ) and (
                robot.position.y < self.height // 2
                if top
                else robot.position.y > self.height // 2
            )

        return math.prod(
            [
                sum(1 for robot in self.robots if in_quadrant(robot, True, True)),  # Q1
                sum(
                    1 for robot in self.robots if in_quadrant(robot, False, True)
                ),  # Q2
                sum(
                    1 for robot in self.robots if in_quadrant(robot, True, False)
                ),  # Q3
                sum(
                    1 for robot in self.robots if in_quadrant(robot, False, False)
                ),  # Q4
            ]
        )


class Day14PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(14, "a")

    def _new_solver(self):
        return Day14PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 12, extra_params={"width": 11, "height": 7})]

    def _main_input_extra_params(self) -> dict[str, Any]:
        return {"width": 101, "height": 103}


if __name__ == "__main__":
    controller = Day14PartAController()
    controller.run()
