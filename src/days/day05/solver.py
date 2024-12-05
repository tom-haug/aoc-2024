from abc import abstractmethod
from typing import Any
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

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
