from __future__ import annotations
from src.shared.controller import Controller
from src.days.day12.solver import AnswerType, Day12Solver, NamedRegion, Plot
from src.shared.file_result import FileResult


class Day12PartASolver(Day12Solver):
    def solve(self) -> AnswerType:
        regions: list[NamedRegion] = self._get_regions()
        return sum(self._calculate_fence_price(region) for _, region in regions)

    def _calculate_fence_price(self, region: set[Plot]) -> int:
        fence_segments = sum(
            self._count_exposed_sides(plot, region) for plot in region
        )
        return fence_segments * len(region)

    def _count_exposed_sides(self, plot: Plot, region: set[Plot]) -> int:
        return sum(neighbor not in region for _, neighbor in plot.neighbors())


class Day12PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(12, "a")

    def _new_solver(self):
        return Day12PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [
            FileResult("sample01.txt", 140),
            FileResult("sample02.txt", 772),
            FileResult("sample03.txt", 1930),
        ]


if __name__ == "__main__":
    controller = Day12PartAController()
    controller.run()
