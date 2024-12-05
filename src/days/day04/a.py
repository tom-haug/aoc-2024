from typing import List, Tuple
from src.shared.controller import Controller
from src.days.day04.solver import AnswerType, Day04Solver
from src.shared.file_result import FileResult


class Day04PartASolver(Day04Solver):
    def solve(self) -> AnswerType:
        count = 0
        for row in range(self.data.shape[0]):
            for col in range(self.data.shape[1]):
                if col < self.data.shape[1] - 3:
                    if self.check_word(
                        [(row, col), (row, col + 1), (row, col + 2), (row, col + 3)]
                    ):
                        count += 1
                    if row > 2 and self.check_word(
                        [
                            (row, col),
                            (row - 1, col + 1),
                            (row - 2, col + 2),
                            (row - 3, col + 3),
                        ]
                    ):
                        count += 1
                    if row < self.data.shape[0] - 3 and self.check_word(
                        [
                            (row, col),
                            (row + 1, col + 1),
                            (row + 2, col + 2),
                            (row + 3, col + 3),
                        ]
                    ):
                        count += 1
                if col > 2:
                    if self.check_word(
                        [(row, col), (row, col - 1), (row, col - 2), (row, col - 3)]
                    ):
                        count += 1
                    if row > 2 and self.check_word(
                        [
                            (row, col),
                            (row - 1, col - 1),
                            (row - 2, col - 2),
                            (row - 3, col - 3),
                        ]
                    ):
                        count += 1
                    if row < self.data.shape[0] - 3 and self.check_word(
                        [
                            (row, col),
                            (row + 1, col - 1),
                            (row + 2, col - 2),
                            (row + 3, col - 3),
                        ]
                    ):
                        count += 1
                if row < self.data.shape[0] - 3 and self.check_word(
                    [(row, col), (row + 1, col), (row + 2, col), (row + 3, col)]
                ):
                    count += 1
                if row > 2 and self.check_word(
                    [(row, col), (row - 1, col), (row - 2, col), (row - 3, col)]
                ):
                    count += 1

        return count

    def check_word(self, coordinates: List[Tuple[int, int]]) -> bool:
        word = ""
        for coord in coordinates:
            word += self.data[coord[0], coord[1]]
        return word == "XMAS"


class Day04PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(4, "a")

    def _new_solver(self):
        return Day04PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 18)]


if __name__ == "__main__":
    controller = Day04PartAController()
    controller.run()
