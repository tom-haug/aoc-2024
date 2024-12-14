from dataclasses import dataclass
from src.shared.controller import Controller
from src.days.day12.solver import AnswerType, Day12Solver, Direction, NamedRegion, Plot
from src.shared.file_result import FileResult


@dataclass
class FenceSegment:
    direction: Direction
    plot: Plot


@dataclass
class FenceSide:
    direction: Direction
    plots: list[Plot]


class Day12PartBSolver(Day12Solver):
    def solve(self) -> AnswerType:
        regions: list[NamedRegion] = self._get_regions()

        total_price = 0
        for _, region in regions:
            fence_segments = self._get_fence_segments(region)
            fence_sides = self._get_fence_sides(fence_segments)
            total_price += len(region) * len(fence_sides)
        return total_price

    def _get_fence_segments(self, region: set[Plot]) -> list[FenceSegment]:
        fence_segments: list[FenceSegment] = []
        for plot in region:
            for direction, neighbor in plot.neighbors():
                if neighbor not in region:
                    fence_segments.append(FenceSegment(direction, plot))
        return fence_segments

    def _get_fence_sides(self, fence_segments: list[FenceSegment]) -> list[FenceSide]:
        fence_sides: list[FenceSide] = []
        remaining_segments = fence_segments.copy()

        while remaining_segments:
            current = remaining_segments.pop(0)
            current_side = FenceSide(current.direction, [current.plot])
            fence_sides.append(current_side)

            # Keep combining segments until no more matches found
            changed = True
            while changed:
                changed = False
                for i in range(len(remaining_segments) - 1, -1, -1):
                    segment = remaining_segments[i]
                    if self._can_combine_with_side(current_side, segment):
                        current_side.plots.append(segment.plot)
                        remaining_segments.pop(i)
                        changed = True

        return fence_sides

    def _can_combine_with_side(self, side: FenceSide, segment: FenceSegment) -> bool:
        # Must be same direction
        if segment.direction != side.direction:
            return False

        # Check if segment is adjacent to any plot in the side
        for existing_plot in side.plots:
            if side.direction in (Direction.Up, Direction.Down):
                if (
                    segment.plot.y == existing_plot.y
                    and abs(segment.plot.x - existing_plot.x) == 1
                ):
                    return True
            else:
                if (
                    segment.plot.x == existing_plot.x
                    and abs(segment.plot.y - existing_plot.y) == 1
                ):
                    return True

        return False


class Day12PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(12, "b")

    def _new_solver(self):
        return Day12PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [
            FileResult("sample01.txt", 80),
            FileResult("sample04.txt", 236),
            FileResult("sample05.txt", 368),
        ]


if __name__ == "__main__":
    controller = Day12PartBController()
    controller.run()
