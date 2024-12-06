from abc import abstractmethod
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int


class Day05Solver(Solver[AnswerType]):
    rules: list[tuple[int, int]]
    # dict of page number to relative position in update
    updates: list[dict[int, int]]

    def initialize(self, file_path: str):
        input = load_text_file(file_path) or ""
        rules_section, updates_section = input.split("\n\n")
        self.rules = [
            (int(rule.split("|")[0]), int(rule.split("|")[1]))
            for rule in rules_section.split("\n")
        ]
        self.updates = [
            {int(page_num): idx for idx, page_num in enumerate(update.split(","))}
            for update in updates_section.split("\n")
        ]

    def _calculate_middle_sum(self, updates: list[dict[int, int]]) -> int:
        return sum(self._middle_page_number(update) for update in updates)

    def _get_updates_in_status(self, correctly_ordered: bool) -> list[dict[int, int]]:
        return [
            update
            for update in self.updates
            if correctly_ordered == self._check_update_satisfies_rules(update)
        ]

    def _middle_page_number(self, update: dict[int, int]) -> int:
        middle_pos = len(update) // 2
        return next(page for page, pos in update.items() if pos == middle_pos)

    def _check_update_satisfies_rules(self, update: dict[int, int]) -> bool:
        return all(
            self._check_update_satisfies_rule(update, rule) for rule in self.rules
        )

    def _check_update_satisfies_rule(
        self, update: dict[int, int], rule: tuple[int, int]
    ) -> bool:
        a_pos, b_pos = rule
        a_idx = update.get(a_pos)
        b_idx = update.get(b_pos)

        if a_idx is None or b_idx is None:
            return True

        return a_idx < b_idx

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
