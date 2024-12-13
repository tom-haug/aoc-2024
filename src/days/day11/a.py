from src.shared.controller import Controller
from src.days.day11.solver import AnswerType, Day11Solver
from src.shared.file_result import FileResult


class Day11PartASolver(Day11Solver):
    def solve(self) -> AnswerType:
        return self._run_simulation(25)


class Day11PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(11, "a")

    def _new_solver(self):
        return Day11PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 55312)]


if __name__ == "__main__":
    controller = Day11PartAController()
    controller.run()
