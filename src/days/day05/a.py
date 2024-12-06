from src.shared.controller import Controller
from src.days.day05.solver import AnswerType, Day05Solver
from src.shared.file_result import FileResult


class Day05PartASolver(Day05Solver):
    def solve(self) -> AnswerType:
        correctly_ordered = self._get_updates_in_status(True)
        return self._calculate_middle_sum(correctly_ordered)


class Day05PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(5, "a")

    def _new_solver(self):
        return Day05PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 143)]


if __name__ == "__main__":
    controller = Day05PartAController()
    controller.run()
