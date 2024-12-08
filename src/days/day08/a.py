from itertools import combinations
from src.shared.controller import Controller
from src.days.day08.solver import AnswerType, Day08Solver, Position
from src.shared.file_result import FileResult


class Day08PartASolver(Day08Solver):
    def solve(self) -> AnswerType:
        antinodes: set[Position] = set()
        for locations in self.frequency_location.values():
            for pos1, pos2 in combinations(locations, 2):
                # Calculate delta between points
                delta = Position(pos2.x - pos1.x, pos2.y - pos1.y)

                # Calculate potential antinode positions
                candidates = [
                    Position(pos1.x - delta.x, pos1.y - delta.y),
                    Position(pos2.x + delta.x, pos2.y + delta.y),
                ]

                # Add valid positions to antinodes
                antinodes.update(
                    pos for pos in candidates if self._is_within_bounds(pos)
                )
        return len(antinodes)


class Day08PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(8, "a")

    def _new_solver(self):
        return Day08PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [
            FileResult("sample01.txt", 2),
            FileResult("sample02.txt", 4),
            FileResult("sample03.txt", 4),
            FileResult("sample04.txt", 14),
        ]


if __name__ == "__main__":
    controller = Day08PartAController()
    controller.run()
