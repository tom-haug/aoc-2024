from src.shared.controller import Controller
from src.days.day16.solver import AnswerType, Day16Solver, PathFinder
from src.shared.file_result import FileResult


class Day16PartBSolver(Day16Solver):
    def solve(self) -> AnswerType:
        path_finder = PathFinder(self.matrix)
        paths = path_finder.astar(self.start, self.goal)
        if paths is not None:
            if self.show_visual:
                for path, cost in paths:
                    self._visualize_path(path)
            unique_tiles = {(node.x, node.y) for path, _ in paths for node in path}
            return len(unique_tiles)
        raise Exception("No path found")


class Day16PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(16, "b")

    def _new_solver(self):
        return Day16PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 45), FileResult("sample02.txt", 64)]


if __name__ == "__main__":
    controller = Day16PartBController()
    controller.run()
