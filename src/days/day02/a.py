from src.shared.controller import Controller
from src.days.day02.solver import AnswerType, Day02Solver
from src.shared.file_result import FileResult


class Day02PartASolver(Day02Solver):
    def solve(self) -> AnswerType:
        result = sum(1 for report in self.reports if self.is_report_safe(report))
        return result

    def is_report_safe(self, report: list[int]) -> bool:
        pairs = zip(report, report[1:])
        asc = report[1] > report[0]

        return all(
            (b > a) == asc and
            1 <= abs(b-a) <= 3
            for a, b in pairs
        )


class Day02PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(2, 'a')

    def _new_solver(self):
        return Day02PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 2)]


if __name__ == "__main__":
    controller = Day02PartAController()
    controller.run()
