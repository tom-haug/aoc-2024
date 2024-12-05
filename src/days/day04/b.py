from typing import List, Tuple
from src.shared.controller import Controller
from src.days.day04.solver import AnswerType, Day04Solver
from src.shared.file_result import FileResult


class Day04PartBSolver(Day04Solver):
    def solve(self) -> AnswerType:
        count = 0
        for row in range(self.data.shape[0]):
            for col in range(self.data.shape[1]):
                if (
                    self.data[row, col] == "A"
                    and 0 < row < self.data.shape[0] - 1
                    and 0 < col < self.data.shape[1] - 1
                ):
                    if self.check_word(
                        [(row - 1, col - 1), (row, col), (row + 1, col + 1)]
                    ) and self.check_word(
                        [(row - 1, col + 1), (row, col), (row + 1, col - 1)]
                    ):
                        count += 1
        return count

    def check_word(self, coordinates: List[Tuple[int, int]]) -> bool:
        word = ""
        for coord in coordinates:
            word += self.data[coord[0], coord[1]]
        return word == "MAS" or word == "SAM"


class Day04PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(4, "b")

    def _new_solver(self):
        return Day04PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 9)]


if __name__ == "__main__":
    controller = Day04PartBController()
    controller.run()
