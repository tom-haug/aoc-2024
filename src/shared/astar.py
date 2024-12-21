# -*- coding: utf-8 -*-
""" generic A-Star path searching algorithm with previous node tracking """

from abc import ABC, abstractmethod
from heapq import heappush, heappop
from typing import Iterable, Union, Optional, Tuple

# infinity as a constant
Infinite = float("inf")

class AStar(ABC):
    __slots__ = ()

    class SearchNode:
        """Representation of a search node with previous node tracking"""

        __slots__ = ("data", "gscore", "fscore", "closed", "came_from", "out_openset", "previous")

        def __init__(
            self, data, gscore: float = Infinite, fscore: float = Infinite
        ) -> None:
            self.data = data
            self.gscore = gscore
            self.fscore = fscore
            self.closed = False
            self.out_openset = True
            self.came_from = None
            self.previous = None  # Track the previous node in path

        def __lt__(self, b: "AStar.SearchNode") -> bool:
            return self.fscore < b.fscore

    class SearchNodeDict(dict):
        def __missing__(self, k):
            v = AStar.SearchNode(k)
            self.__setitem__(k, v)
            return v

    @abstractmethod
    def heuristic_cost_estimate(self, current, goal) -> float:
        """Computes the estimated (rough) distance between a node and the goal"""
        raise NotImplementedError

    @abstractmethod
    def distance_between(self, n1, n2, prev: Optional = None) -> float:
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

    def is_goal_reached(self, current, goal) -> bool:
        """returns true when we can consider that 'current' is the goal"""
        return current == goal

    def reconstruct_path(self, last, reversePath=False) -> tuple[Iterable, float]:
        """Reconstructs the path and calculates total cost.
        
        Returns:
            tuple: (path_iterable, total_cost)
        """
        def _gen():
            current = last
            while current:
                yield current.data
                current = current.came_from
                
        # The total cost is stored in the gscore of the last node
        total_cost = last.gscore
        
        if reversePath:
            return _gen(), total_cost
        else:
            return reversed(list(_gen())), total_cost

    def astar(self, start, goal, reversePath: bool = False) -> Union[tuple[Iterable, float], None]:
        """Find the optimal path and its total cost.
        
        Returns:
            tuple: (path_iterable, total_cost) if path found, None if no path exists
        """
        if self.is_goal_reached(start, goal):
            return [start], 0.0
        
        searchNodes = AStar.SearchNodeDict()
        startNode = searchNodes[start] = AStar.SearchNode(
            start, gscore=0.0, fscore=self.heuristic_cost_estimate(start, goal)
        )
        startNode.previous = None  # Explicitly set start node's previous to None
        
        openSet: list = []
        heappush(openSet, startNode)
        
        while openSet:
            current = heappop(openSet)
            
            # print(current.data, current.gscore, current.fscore)

            if self.is_goal_reached(current.data, goal):
                return self.reconstruct_path(current, reversePath)
                
            current.out_openset = True
            current.closed = True
            
            for neighbor in map(lambda n: searchNodes[n], self.neighbors(current.data)):
                if neighbor.closed:
                    continue
                    
                # Get the previous node for distance calculation
                prev_node = current.previous.data if current.previous else None
                
                tentative_gscore = current.gscore + self.distance_between(
                    current.data, neighbor.data, prev_node
                )
                
                if tentative_gscore >= neighbor.gscore:
                    continue
                    
                neighbor.came_from = current
                neighbor.previous = current  # Update the previous node reference
                neighbor.gscore = tentative_gscore
                neighbor.fscore = tentative_gscore + self.heuristic_cost_estimate(
                    neighbor.data, goal
                )
                
                if neighbor.out_openset:
                    neighbor.out_openset = False
                    heappush(openSet, neighbor)
                else:
                    # re-add the node in order to re-sort the heap
                    openSet.remove(neighbor)
                    heappush(openSet, neighbor)
        
        return None


def find_path(
    start,
    goal,
    neighbors_fnct,
    reversePath=False,
    heuristic_cost_estimate_fnct=lambda a, b: Infinite,
    distance_between_fnct=lambda a, b, prev=None: 1.0,
    is_goal_reached_fnct=lambda a, b: a == b,
):
    """A non-class version of the path finding algorithm"""

    class FindPath(AStar):
        def heuristic_cost_estimate(self, current, goal):
            return heuristic_cost_estimate_fnct(current, goal)

        def distance_between(self, n1, n2, prev=None):
            return distance_between_fnct(n1, n2, prev)

        def neighbors(self, node):
            return neighbors_fnct(node)

        def is_goal_reached(self, current, goal):
            return is_goal_reached_fnct(current, goal)

    return FindPath().astar(start, goal, reversePath)


__all__ = ["AStar", "find_path"]