from collections import deque
from src.shared.controller import Controller
from src.days.day09.solver import AnswerType, Day09Solver
from src.shared.file_loading import load_text_file
from src.shared.file_result import FileResult


class Day09PartASolver(Day09Solver):
    raw_data: deque[int | None]

    def initialize(self, file_path: str):
        input = load_text_file(file_path) or ""
        self.raw_data = deque()
        for idx, char in enumerate(input):
            id = int(idx / 2) if (idx % 2) == 0 else None
            self.raw_data.extend([id] * int(char))

    def solve(self) -> AnswerType:
        compacated: list[int] = []
        while len(self.raw_data) > 0:
            current = self.raw_data.popleft()
            while current is None and len(self.raw_data) > 0:
                current = self.raw_data.pop()
            if current is not None:
                compacated.append(current)
        return self._calculate_checksum(compacated)

    def _calculate_checksum(self, data: list[int]) -> int:
        return sum(idx * value for idx, value in enumerate(data))


class Day09PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(9, "a")

    def _new_solver(self):
        return Day09PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 1928)]


if __name__ == "__main__":
    controller = Day09PartAController()
    controller.run()
