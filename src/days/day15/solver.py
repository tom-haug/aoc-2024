from __future__ import annotations
from abc import abstractmethod
from enum import Enum
import os
import time
from typing import NamedTuple

import numpy as np
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int


class Point(NamedTuple):
    x: int
    y: int


class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3


class Day15Solver(Solver[AnswerType]):
    walls: set[Point]
    boxes: set[Point]
    robot: Point
    instructions: list[Direction]
    width: int
    height: int

    @property
    @abstractmethod
    def x_scale_factor(self) -> int:
        ...

    @property
    def visual_available(self) -> bool:
        return True

    def initialize(self, file_path: str):
        input = load_text_file(file_path) or ""
        map, instructions = input.split("\n\n")
        self.width = len(map.split("\n")[0]) * self.x_scale_factor
        self.height = len(map.split("\n"))
        self.walls = set()
        self.boxes = set()
        for y, line in enumerate(map.split("\n")):
            for x, char in enumerate(line):
                if char == "#":
                    self.walls.add(Point(x * self.x_scale_factor, y))
                elif char == "O":
                    self.boxes.add(Point(x * self.x_scale_factor, y))
                elif char == "@":
                    self.robot = Point(x * self.x_scale_factor, y)

        self.instructions = []
        for char in instructions:
            match char:
                case "^":
                    self.instructions.append(Direction.Up)
                case ">":
                    self.instructions.append(Direction.Right)
                case "v":
                    self.instructions.append(Direction.Down)
                case "<":
                    self.instructions.append(Direction.Left)

    def solve(self) -> AnswerType:
        for round, instruction in enumerate(self.instructions):
            self._run_instruction(instruction)
            if self.show_visual:
                self._print_matrix(round)
                time.sleep(1)
        return self._calculate_gps_sum()

    def _run_instruction(self, instruction: Direction):
        if self._try_move(self.robot, instruction, True, 1):
            self._try_move(self.robot, instruction, False, 1)
            self.robot = self._get_relative(self.robot, instruction)

    def _try_move(
        self, point: Point, direction: Direction, check_only: bool, obj_width: int
    ) -> bool:
        match direction:
            case Direction.Up | Direction.Down:
                # Get all positions that could contain a wall or box in the direction of movement
                positions = []
                first_pos = self._get_relative(point, direction)
                for offset in range(self.x_scale_factor):
                    positions.append(
                        self._get_relative(first_pos, Direction.Left, offset)
                    )

                # Check for walls
                if any(pos in self.walls for pos in positions):
                    return False

                # Check each position for boxes
                for pos in positions:
                    if pos in self.boxes:
                        # If we find a box, all positions it occupies must be able to move
                        result = True
                        box_pos = pos
                        for _ in range(self.x_scale_factor):
                            result = result and self._try_move(
                                box_pos, direction, check_only, self.x_scale_factor
                            )
                            box_pos = self._get_relative(box_pos, Direction.Right)

                        if not check_only and result:
                            self.boxes.remove(pos)
                            self.boxes.add(self._get_relative(pos, direction))
                        return result

                return True
            case Direction.Left | Direction.Right:
                # For Left, check object width to the left (walls or boxes will have variable width)
                # For Right, check the space after the current object (player has width of 1)
                spaces_to_check = (
                    self.x_scale_factor if direction == Direction.Left else obj_width
                )
                check = self._get_relative(point, direction, spaces_to_check)

                if check in self.walls:
                    return False

                if check in self.boxes:
                    result = self._try_move(
                        check, direction, check_only, self.x_scale_factor
                    )
                    if not check_only and result:
                        self.boxes.remove(check)
                        self.boxes.add(self._get_relative(check, direction))
                    return result

                return True

    def _get_relative(
        self, point: Point, direction: Direction, amount: int = 1
    ) -> Point:
        match direction:
            case Direction.Up:
                return Point(point.x, point.y - amount)
            case Direction.Right:
                return Point(point.x + amount, point.y)
            case Direction.Down:
                return Point(point.x, point.y + amount)
            case Direction.Left:
                return Point(point.x - amount, point.y)

    def _calculate_gps_sum(self) -> int:
        return sum(box.y * 100 + box.x for box in self.boxes)

    def _print_matrix(self, round: int):
        grid = np.full((self.height, self.width), " ")
        for wall in self.walls:
            for i in range(self.x_scale_factor):
                grid[wall.y, wall.x + i] = "#"

        for box in self.boxes:
            if self.x_scale_factor == 1:
                grid[box.y, box.x] = "O"
            else:
                grid[box.y, box.x] = "["
                grid[box.y, box.x + 1] = "]"
        grid[self.robot.y, self.robot.x] = "@"
        os.system("clear")
        print(f"Round: {round}")
        arrow = (
            "^"
            if self.instructions[round] == Direction.Up
            else (
                ">"
                if self.instructions[round] == Direction.Right
                else ("v" if self.instructions[round] == Direction.Down else "<")
            )
        )
        print(f"Instruction: {arrow}")
        for row in grid:
            print("".join(row))
