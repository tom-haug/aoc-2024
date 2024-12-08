from src.shared.controller import Controller
from src.days.day07.solver import AnswerType, Day07Solver
from src.shared.file_result import FileResult


class Day07PartASolver(Day07Solver):
    def solve(self) -> AnswerType:
        valid_equations = [
            equation
            for equation in self.equations
            if self.recurse(equation.operands, 0, 0, equation.answer)
        ]
        return sum(equation.answer for equation in valid_equations)

    def recurse(
        self, operands: list[int], index: int, cur_total: int, answer: int
    ) -> bool:
        if index >= len(operands):
            return cur_total == answer
        else:
            return self.recurse(
                operands, index + 1, cur_total + operands[index], answer
            ) or self.recurse(operands, index + 1, cur_total * operands[index], answer)


class Day07PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(7, "a")

    def _new_solver(self):
        return Day07PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 3749)]


if __name__ == "__main__":
    controller = Day07PartAController()
    controller.run()
