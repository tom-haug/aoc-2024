from abc import abstractmethod
from dataclasses import dataclass
import os
import time
from typing import NamedTuple

import numpy as np
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Point(NamedTuple):
    x: int
    y: int


@dataclass
class Robot:
    position: Point
    velocity: Point

    def move(self, width: int, height: int):
        x = (self.position.x + self.velocity.x) % width
        y = (self.position.y + self.velocity.y) % height
        self.position = Point(x, y)


class Day14Solver(Solver[AnswerType]):
    robots: list[Robot]
    width: int
    height: int

    @property
    def visual_available(self) -> bool:
        return True

    def initialize_extra_params(self, extra_params: dict[str, str]):
        super().initialize_extra_params(extra_params)
        self.width = int(extra_params["width"])
        self.height = int(extra_params["height"])

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path)
        self.robots = []
        for line in input:
            sections = line.split(" ")
            position_parts = sections[0][2:].split(",")
            velocity_parts = sections[1][2:].split(",")
            position = Point(int(position_parts[0]), int(position_parts[1]))
            velocity = Point(int(velocity_parts[0]), int(velocity_parts[1]))
            self.robots.append(Robot(position, velocity))

    def _run_simulation(self, rounds: int):
        for round in range(1, rounds + 1):
            for robot in self.robots:
                robot.move(self.width, self.height)
            if self.show_visual:
                self._print_matrix(round)
                time.sleep(0.1)

    def _print_matrix(self, round: int):
        grid = np.full((self.height, self.width), " ")
        for robot in self.robots:
            grid[robot.position.y, robot.position.x] = "#"
        os.system("clear")
        print(f"Round: {round}")
        for row in grid:
            print("".join(row))

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
