from abc import abstractmethod

from nptyping import NDArray
import numpy as np
from src.days.day16.astar import AStar, Direction, PathNode
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class PathFinder(AStar):
    matrix: NDArray
    width: int
    height: int

    def __init__(self, matrix: NDArray):
        self.matrix = matrix
        self.height, self.width = matrix.shape

    def heuristic_cost_estimate(self, current: PathNode, goal: PathNode) -> float:
        dx = abs(goal.x - current.x)
        dy = abs(goal.y - current.y)
        min_turns = 0

        # If we're moving horizontally (East/West)
        if current.incoming_direction in (Direction.East, Direction.West):
            # If we need to move vertically at all, that's one turn
            if dy > 0:
                min_turns += 1
        # If we're moving vertically (North/South)
        else:
            # If we need to move horizontally at all, that's one turn
            if dx > 0:
                min_turns += 1

        return (min_turns * 1000) + dx + dy

    def distance_between(self, current: PathNode, next: PathNode) -> float:
        next_direction = self._get_direction(current, next)
        if current.incoming_direction == next_direction:
            return 1
        else:
            return 1001

    def _get_direction(self, current: PathNode, next: PathNode) -> Direction:
        # If x values are different, we're moving horizontally
        if current.x != next.x:
            return Direction.East if next.x > current.x else Direction.West
        # If y values are different, we're moving vertically
        if current.y != next.y:
            return Direction.South if next.y > current.y else Direction.North

        raise ValueError("Current and next nodes are the same position")

    def neighbors(self, node: PathNode) -> list[PathNode]:
        x, y = node.x, node.y
        neighbor_positions = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

        neighbors_list = []
        for x2, y2 in neighbor_positions:
            if (
                0 <= x2 < self.width
                and 0 <= y2 < self.height
                and self.matrix[y2, x2] in [".", "E"]
            ):
                # Create PathNode with direction calculated from current to this neighbor
                neighbor = PathNode(x2, y2)
                incoming_dir = self._get_direction(node, neighbor)
                neighbors_list.append(PathNode(x2, y2, incoming_dir))

        return neighbors_list


class Day16Solver(Solver[AnswerType]):
    matrix: NDArray
    start: PathNode
    goal: PathNode

    @property
    def visual_available(self) -> bool:
        return True

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.matrix = np.array([[char for char in line] for line in input])
        start_row, start_col = np.where(self.matrix == "S")
        goal_row, goal_col = np.where(self.matrix == "E")
        self.start = PathNode(start_col[0], start_row[0], Direction.East)
        self.goal = PathNode(goal_col[0], goal_row[0])

    def _visualize_path(self, path: list[PathNode]) -> None:
        """Visualizes the path with arrows showing the direction taken to enter each node"""
        # Create a copy of the matrix to mark the path
        viz_matrix = np.full_like(self.matrix, ".")
        viz_matrix[self.matrix == "#"] = "#"  # Add walls

        # Direction to arrow mapping
        direction_to_arrow = {
            Direction.North: "^",
            Direction.South: "v",
            Direction.East: ">",
            Direction.West: "<",
        }

        # Mark each node in the path with its incoming direction
        for node in path:
            viz_matrix[node.y, node.x] = direction_to_arrow[node.incoming_direction]

        # Mark start and end
        viz_matrix[self.start.y, self.start.x] = "S"
        viz_matrix[self.goal.y, self.goal.x] = "E"

        # Print the visualization
        print("\nPath visualization:")
        for row in viz_matrix:
            print("".join(row))

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
