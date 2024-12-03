from src.shared.controller import Controller
from src.days.day01.solver import AnswerType, Day01Solver
from src.shared.file_result import FileResult


class Day01PartBSolver(Day01Solver):
    def solve(self) -> AnswerType:
        result = 0
        for val in self.list_a:
            b_occurances = self.list_b.count(val)
            result += b_occurances * val
        return result


class Day01PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(1, 'b')

    def _new_solver(self):
        return Day01PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 31)]


if __name__ == "__main__":
    controller = Day01PartBController()
    controller.run()
