from itertools import combinations
from src.shared.controller import Controller
from src.days.day08.solver import AnswerType, Day08Solver, Position
from src.shared.file_result import FileResult


class Day08PartBSolver(Day08Solver):
    def solve(self) -> AnswerType:
        antinodes: set[Position] = set()

        for locations in self.frequency_location.values():
            for pos1, pos2 in combinations(locations, 2):
                # Calculate delta between points
                delta = Position(pos2.x - pos1.x, pos2.y - pos1.y)

                # Find antinodes on or before pos1
                test_position = pos1
                while self._is_within_bounds(test_position):
                    antinodes.add(test_position)
                    test_position = Position(
                        test_position.x - delta.x, test_position.y - delta.y
                    )

                # Find antinodes on or after pos2
                test_position = pos2
                while self._is_within_bounds(test_position):
                    antinodes.add(test_position)
                    test_position = Position(
                        test_position.x + delta.x, test_position.y + delta.y
                    )

        return len(antinodes)


class Day08PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(8, "b")

    def _new_solver(self):
        return Day08PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [
            FileResult("sample05.txt", 9),
            FileResult("sample04.txt", 34),
        ]


if __name__ == "__main__":
    controller = Day08PartBController()
    controller.run()
