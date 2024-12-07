from src.shared.controller import Controller
from src.days.day06.solver import AnswerType, Day06Solver, move, Position, Direction
from src.shared.file_result import FileResult


class Day06PartBSolver(Day06Solver):
    def solve(self) -> AnswerType:
        guard_position = self.original_guard_position
        guard_direction = self.original_guard_direction
        visited_positions: dict[Position, set[Direction]] = dict()
        looping_obstructions: set[Position] = set()

        while (
            0 <= guard_position.x <= self.map_width - 1
            and 0 <= guard_position.y <= self.map_height - 1
        ):
            possible_obstruction_position = move(guard_position, guard_direction)
            if (
                0 <= possible_obstruction_position.x <= self.map_width - 1
                and 0 <= possible_obstruction_position.y <= self.map_height - 1
                and possible_obstruction_position not in visited_positions
                and possible_obstruction_position not in self.obstructions
                and possible_obstruction_position not in looping_obstructions
                and possible_obstruction_position != self.original_guard_position
                and self._check_is_loop(
                    self.obstructions.union({possible_obstruction_position}),
                    visited_positions,
                    guard_position,
                    guard_direction,
                )
            ):
                looping_obstructions.add(possible_obstruction_position)

            if guard_position in visited_positions:
                visited_positions[guard_position].add(guard_direction)
            else:
                visited_positions[guard_position] = {guard_direction}

            next_position = move(guard_position, guard_direction)

            if next_position in self.obstructions:
                guard_direction = guard_direction.turn_right()
            else:
                guard_position = next_position

        return len(looping_obstructions)

    def _check_is_loop(
        self,
        obstructions: set[Position],
        visited_positions: dict[Position, set[Direction]],
        starting_guard_position: Position,
        starting_guard_direction: Direction,
    ) -> bool:
        guard_position = starting_guard_position
        guard_direction = starting_guard_direction
        test_visited_positions = {k: v.copy() for k, v in visited_positions.items()}

        while (
            0 <= guard_position.x <= self.map_width - 1
            and 0 <= guard_position.y <= self.map_height - 1
        ):
            if (
                guard_position in test_visited_positions
                and guard_direction in test_visited_positions[guard_position]
            ):
                return True
            elif guard_position in test_visited_positions:
                test_visited_positions[guard_position].add(guard_direction)
            else:
                test_visited_positions[guard_position] = {guard_direction}

            next_position = move(guard_position, guard_direction)

            if next_position in obstructions:
                guard_direction = guard_direction.turn_right()
            else:
                guard_position = next_position
        return False


class Day06PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(6, "b")

    def _new_solver(self):
        return Day06PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 6)]


if __name__ == "__main__":
    controller = Day06PartBController()
    controller.run()
