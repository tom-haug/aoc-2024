from src.shared.controller import Controller
from src.days.day13.solver import AnswerType, Day13Solver
from src.shared.file_result import FileResult


class Day13PartBSolver(Day13Solver):
    def solve(self) -> AnswerType:
        for machine in self.machines:
            machine.prize.x += 10000000000000
            machine.prize.y += 10000000000000
        tokens = sum(self._calc_min_tokens(machine, None) for machine in self.machines)
        return tokens


class Day13PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(13, "b")

    def _new_solver(self):
        return Day13PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [
            FileResult("sample01.txt", 0),
            # FileResult("sample02.txt", 0),
            FileResult("sample03.txt", 0),
            # FileResult("sample04.txt", 0),
        ]


if __name__ == "__main__":
    controller = Day13PartBController()
    controller.run()
