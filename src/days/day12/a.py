from __future__ import annotations
from src.shared.controller import Controller
from src.days.day12.solver import AnswerType, Day12Solver, NamedRegion, Region, Plot
from src.shared.file_result import FileResult


class Day12PartASolver(Day12Solver):
    def solve(self) -> AnswerType:
        regions: list[NamedRegion] = []

        while self.plots:
            plot = next(iter(self.plots))
            plant_type = self.plots[plot]
            region = self._find_touching_plots(plot, plant_type)
            regions.append((plant_type, region))

        return sum(self._calculate_fence_price(region) for _, region in regions)

    def _calculate_fence_price(self, region: Region) -> int:
        total_exposed_sides = sum(
            self._count_exposed_sides(plot, region) for plot in region
        )
        return total_exposed_sides * len(region)

    def _count_exposed_sides(self, plot: Plot, region: Region) -> int:
        return sum(neighbor not in region for neighbor in plot.neighbors())

    def _find_touching_plots(self, start: Plot, plant_type: str) -> Region:
        if start not in self.plots or self.plots[start] != plant_type:
            return set()

        region: Region = set()
        queue = [start]

        while queue:
            plot = queue.pop(0)
            if plot not in region:
                region.add(plot)
                self.plots.pop(plot)

                queue.extend(
                    neighbor
                    for neighbor in plot.neighbors()
                    if (
                        neighbor in self.plots
                        and self.plots[neighbor] == plant_type
                        and neighbor not in region
                    )
                )

        return region


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
