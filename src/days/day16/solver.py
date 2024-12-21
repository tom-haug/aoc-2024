from abc import abstractmethod
from enum import Enum
import math
from typing import Any, NamedTuple

from nptyping import NDArray
import numpy as np
from src.shared.astar import AStar
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int
class Point(NamedTuple):
    x: int
    y: int
    
class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3
    
class PathFinder(AStar):
    matrix: NDArray
    width: int
    height: int

    def __init__(self, matrix: NDArray):
        self.matrix = matrix
        self.height, self.width = matrix.shape

    def heuristic_cost_estimate(self, current: Point, goal: Point) -> float:
        (x1, y1) = current
        (x2, y2) = goal
        return math.hypot(x2 - x1, y2 - y1)

    def distance_between(self, current: Point, next: Point, prev: Point) -> float:
        current_direction = Direction.Right if prev is None else self._get_direction(prev, current)
        next_direction = self._get_direction(current, next)
        if current_direction == next_direction:
            return 1
        else:
            return 1001

    def _get_direction(self, current: Point, next: Point) -> Direction | None:
        # If x values are different, we're moving horizontally
        if current.x != next.x:
            return Direction.Right if next.x > current.x else Direction.Left
        # If y values are different, we're moving vertically
        if current.y != next.y:
            return Direction.Down if next.y > current.y else Direction.Up
        
        return None

    def neighbors(self, node: Point) -> list[Point]:
        x, y = node
        return [
            Point(x2, y2)
            for x2, y2 in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
            if 0 <= x2 < self.width
            and 0 <= y2 < self.height
            and self.matrix[y2, x2] in ['.', 'E']
        ]

    def minimum_cost(self, start: Point, end: Point) -> int:
        solution = self.astar(start, end)
        if solution is None:
            return -1
        else:
            _, cost = solution
            return int(cost)


class Day16Solver(Solver[AnswerType]):
    matrix: NDArray
    start: Point
    goal: Point

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.matrix = np.array(
            [
                [char for char in line]
                for line in input
            ]
        )
        start_row, start_col = np.where(self.matrix == 'S')
        goal_row, goal_col = np.where(self.matrix == 'E')
        self.start = Point(start_col[0], start_row[0])
        self.goal = Point(goal_col[0], goal_row[0])

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
