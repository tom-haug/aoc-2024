from src.shared.controller import Controller
from src.days.day05.solver import AnswerType, Day05Solver
from src.shared.file_result import FileResult


class Day05PartBSolver(Day05Solver):
    def solve(self) -> AnswerType:
        updates = self._get_updates_in_status(False)
        self._fix_updates(updates)
        return self._calculate_middle_sum(updates)

    def _fix_updates(self, updates: list[dict[int, int]]) -> None:
        for update in updates:
            while True:
                if not any(self._fix_update(update, rule) for rule in self.rules):
                    break

    def _fix_update(self, update: dict[int, int], rule: tuple[int, int]) -> bool:
        a_pos, b_pos = rule
        a_idx = update.get(a_pos)
        b_idx = update.get(b_pos)

        if a_idx is None or b_idx is None:
            return False

        if a_idx > b_idx:
            update[a_pos], update[b_pos] = b_idx, a_idx
            return True

        return False


class Day05PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(5, "b")

    def _new_solver(self):
        return Day05PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 123)]


if __name__ == "__main__":
    controller = Day05PartBController()
    controller.run()
