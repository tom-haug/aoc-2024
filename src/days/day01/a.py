from src.shared.controller import Controller
from src.days.day01.solver import AnswerType, Day01Solver
from src.shared.file_result import FileResult


class Day01PartASolver(Day01Solver):
    def initialize(self, file_path: str):
        super().initialize(file_path)
        self.list_a.sort()
        self.list_b.sort()

    def solve(self) -> AnswerType:
        sum = 0
        for idx in range(len(self.list_a)):
            diff = self.list_a[idx] - self.list_b[idx]
            sum += abs(diff)
        return sum


class Day01PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(1, 'a')

    def _new_solver(self):
        return Day01PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 11)]


if __name__ == "__main__":
    controller = Day01PartAController()
    controller.run()
