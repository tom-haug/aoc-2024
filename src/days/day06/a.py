from src.shared.controller import Controller
from src.days.day06.solver import AnswerType, Day06Solver, move, Position, Direction
from src.shared.file_result import FileResult


class Day06PartASolver(Day06Solver):
    def solve(self) -> AnswerType:
        visited_positions: dict[Position, set[Direction]] = dict()
        guard_position = self.original_guard_position
        guard_direction = self.original_guard_direction

        while (
            0 <= guard_position.x <= self.map_width - 1
            and 0 <= guard_position.y <= self.map_height - 1
        ):
            if guard_position in visited_positions:
                visited_positions[guard_position].add(guard_direction)
            else:
                visited_positions[guard_position] = {guard_direction}

            next_position = move(guard_position, guard_direction)

            if next_position in self.obstructions:
                guard_direction = guard_direction.turn_right()
            else:
                guard_position = next_position
        return len(visited_positions)


class Day06PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(6, "a")

    def _new_solver(self):
        return Day06PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 41)]


if __name__ == "__main__":
    controller = Day06PartAController()
    controller.run()
