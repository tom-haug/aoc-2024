# -*- coding: utf-8 -*-
""" generic A-Star path searching algorithm with previous node tracking """

from abc import ABC, abstractmethod
from enum import Enum
from heapq import heappush, heappop
from typing import NamedTuple

# infinity as a constant
Infinite = float("inf")


class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3


class PathNode(NamedTuple):
    x: int
    y: int
    incoming_direction: Direction = Direction.East  # Default for start node


class AStar(ABC):
    __slots__ = ()

    class SearchNode:
        """Representation of a search node with tracking of multiple previous paths"""

        __slots__ = ("data", "gscore", "fscore", "closed", "came_froms", "out_openset")

        def __init__(
            self, data, gscore: float = Infinite, fscore: float = Infinite
        ) -> None:
            self.data = data
            self.gscore = gscore
            self.fscore = fscore
            self.closed = False
            self.out_openset = True
            self.came_froms: list[
                PathNode
            ] = []  # List of nodes we came from with equal optimal cost

        def __lt__(self, b: "AStar.SearchNode") -> bool:
            return self.fscore < b.fscore

    class SearchNodeDict(dict):
        def __missing__(self, k: PathNode):
            v = AStar.SearchNode(k)
            self.__setitem__(k, v)
            return v

    @abstractmethod
    def heuristic_cost_estimate(self, current, goal) -> float:
        """Computes the estimated (rough) distance between a node and the goal"""
        raise NotImplementedError

    @abstractmethod
    def distance_between(self, n1, n2) -> float:
        """Gives the real distance between two adjacent nodes n1 and n2.
        Now includes optional previous node information for more complex distance calculations.

        Args:
            n1: Current node
            n2: Next node
            prev: Previous node in the path (can be None for start node)
        """
        raise NotImplementedError

    @abstractmethod
    def neighbors(self, node):
        """For a given node, returns (or yields) the list of its neighbors"""
        raise NotImplementedError

    def is_goal_reached(self, current: PathNode, goal: PathNode) -> bool:
        """returns true when we reach the goal coordinates, regardless of direction"""
        return current.x == goal.x and current.y == goal.y

    def reconstruct_path(
        self, last, reversePath=False
    ) -> list[tuple[list[PathNode], float]]:
        """Reconstructs all possible paths that reach this node with the optimal cost.

        Returns:
            list[tuple[list[PathNode], float]]: List of (path, total_cost) pairs
        """

        def build_paths(node) -> list[list[PathNode]]:
            if not node.came_froms:
                return [[node.data]]

            paths = []
            for came_from in node.came_froms:
                # Recursively get all paths from previous nodes
                previous_paths = build_paths(came_from)
                # Add current node to each path
                for path in previous_paths:
                    paths.append(path + [node.data])
            return paths

        # Get all possible paths
        paths = build_paths(last)
        total_cost = last.gscore

        # Reverse paths if needed
        if not reversePath:
            for path in paths:
                path.reverse()

        return [(path, total_cost) for path in paths]

    def astar(
        self, start, goal, reversePath: bool = False
    ) -> list[tuple[list[PathNode], float]] | None:
        """Find all optimal paths and their total cost.

        Returns:
            list[tuple[list[PathNode], float]]: List of (path, total_cost) for all optimal paths,
            or None if no path exists
        """
        if self.is_goal_reached(start, goal):
            return [([start], 0.0)]

        searchNodes = AStar.SearchNodeDict()
        startNode = searchNodes[start] = AStar.SearchNode(
            start, gscore=0.0, fscore=self.heuristic_cost_estimate(start, goal)
        )

        openSet: list = []
        heappush(openSet, startNode)
        goal_nodes = []  # Store all goal nodes with optimal cost
        best_cost = Infinite

        while openSet:
            current = heappop(openSet)

            # If we've found a path to goal and this path is worse than our best, skip it
            if best_cost < current.gscore:
                continue

            if self.is_goal_reached(current.data, goal):
                if current.gscore < best_cost:
                    # Found a better path, clear previous paths
                    goal_nodes = [current]
                    best_cost = current.gscore
                elif current.gscore == best_cost:
                    # Found another optimal path
                    goal_nodes.append(current)
                continue

            for neighbor in map(lambda n: searchNodes[n], self.neighbors(current.data)):
                tentative_gscore = current.gscore + self.distance_between(
                    current.data, neighbor.data
                )

                if tentative_gscore > neighbor.gscore and neighbor.gscore != Infinite:
                    # Found a worse path, mark as closed
                    neighbor.closed = True
                    continue

                if tentative_gscore < neighbor.gscore:
                    # Found a better path, clear previous paths
                    neighbor.came_froms = [current]
                    neighbor.gscore = tentative_gscore
                    neighbor.fscore = tentative_gscore + self.heuristic_cost_estimate(
                        neighbor.data, goal
                    )
                    neighbor.closed = False  # Reset closed status
                    neighbor.out_openset = False
                    heappush(openSet, neighbor)
                elif tentative_gscore == neighbor.gscore:
                    # Only add if this came_from isn't already in the list
                    if current not in neighbor.came_froms:
                        neighbor.came_froms.append(current)
                        neighbor.closed = False  # Reset closed status
                        if neighbor.out_openset:
                            neighbor.out_openset = False
                        # Re-add to openSet since we found a new path
                        heappush(openSet, neighbor)

        if not goal_nodes:
            return None

        # Collect all paths from all goal nodes
        all_paths = []
        for goal_node in goal_nodes:
            paths = self.reconstruct_path(goal_node, reversePath)
            all_paths.extend(paths)

        return all_paths


def find_path(
    start,
    goal,
    neighbors_fnct,
    reversePath=False,
    heuristic_cost_estimate_fnct=lambda a, b: Infinite,
    distance_between_fnct=lambda a, b: 1.0,
    is_goal_reached_fnct=lambda a, b: a == b,
):
    """A non-class version of the path finding algorithm"""

    class FindPath(AStar):
        def heuristic_cost_estimate(self, current, goal):
            return heuristic_cost_estimate_fnct(current, goal)

        def distance_between(self, n1, n2):
            return distance_between_fnct(n1, n2)

        def neighbors(self, node):
            return neighbors_fnct(node)

        def is_goal_reached(self, current, goal):
            return is_goal_reached_fnct(current, goal)

    return FindPath().astar(start, goal, reversePath)


__all__ = ["AStar", "find_path"]
