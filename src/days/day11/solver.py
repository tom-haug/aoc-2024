from __future__ import annotations
from abc import abstractmethod
from functools import lru_cache
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file
from math import log10, floor


AnswerType = int


class Day11Solver(Solver[AnswerType]):
    stones: list[int]

    def initialize(self, file_path: str):
        input = load_text_file(file_path) or ""
        self.stones = [int(stone) for stone in input.split(" ")]

    def _run_simulation(self, num_rounds: int) -> int:
        cur_stones = self.stones
        for _ in range(num_rounds):
            next_stones: list[int] = []
            for stone in cur_stones:
                if stone == 0:
                    next_stones.append(1)
                    continue

                num_digits = floor(log10(stone)) + 1
                if num_digits % 2 == 0:
                    half_digits = num_digits // 2
                    divisor = 10**half_digits
                    next_stones.append(stone // divisor)
                    next_stones.append(stone % divisor)
                    continue

                next_stones.append(stone * 2024)
            cur_stones = next_stones
        return len(cur_stones)

    def _run_simulation_dp(self, num_rounds: int) -> int:
        return sum(self._recurse(stone, num_rounds, 0) for stone in self.stones)

    @lru_cache(None)
    def _recurse(self, stone: int, max_rounds: int, cur_round: int) -> int:
        if cur_round >= max_rounds:
            return 1

        if stone == 0:
            return self._recurse(1, max_rounds, cur_round + 1)

        num_digits = floor(log10(stone)) + 1
        if num_digits % 2 == 0:
            half_digits = num_digits // 2
            divisor = 10**half_digits
            return self._recurse(
                stone // divisor, max_rounds, cur_round + 1
            ) + self._recurse(stone % divisor, max_rounds, cur_round + 1)

        return self._recurse(stone * 2024, max_rounds, cur_round + 1)

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
