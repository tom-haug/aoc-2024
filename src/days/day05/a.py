from src.shared.controller import Controller
from src.days.day05.solver import AnswerType, Day05Solver
from src.shared.file_result import FileResult


class Day05PartASolver(Day05Solver):
    def solve(self) -> AnswerType:
        count = sum(
            self.middle_page_number(update)
            for update in self.updates
            if self.check_update_satisfies_rules(update)
        )
        return count

    def check_update_satisfies_rules(self, update: dict[int, int]) -> bool:
        for rule in self.rules:
            if not self.check_update_satisfies_rule(update, rule):
                return False
        return True

    def check_update_satisfies_rule(
        self, update: dict[int, int], rule: tuple[int, int]
    ) -> bool:
        a_idx = update.get(rule[0], -1)
        b_idx = update.get(rule[1], -1)
        return a_idx == -1 or b_idx == -1 or a_idx < b_idx

    def middle_page_number(self, update: dict[int, int]) -> int:
        middle = len(update) // 2
        middle_page = next(
            page_num for page_num, position in update.items() if position == middle
        )
        return middle_page


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
