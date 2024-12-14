from abc import abstractmethod
from dataclasses import dataclass
import re
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = int


@dataclass
class XYPair:
    x: int
    y: int


@dataclass
class MachineConfig:
    button_a: XYPair
    button_b: XYPair
    prize: XYPair


class Day13Solver(Solver[AnswerType]):
    machines: list[MachineConfig]

    def initialize(self, file_path: str):
        input = load_text_file(file_path) or ""
        self.machines = []
        sections = [section for section in input.split("\n\n")]
        for section in sections:
            button_a_section, button_b_section, prize_section = section.split("\n")
            button_a = XYPair(*map(int, re.findall(r"\d+", button_a_section)))
            button_b = XYPair(*map(int, re.findall(r"\d+", button_b_section)))
            prize = XYPair(*map(int, re.findall(r"\d+", prize_section)))
            self.machines.append(MachineConfig(button_a, button_b, prize))

    def _calc_min_tokens(self, machine: MachineConfig, max_pressed: int | None) -> int:
        ax, ay = machine.button_a.x, machine.button_a.y
        bx, by = machine.button_b.x, machine.button_b.y
        px, py = machine.prize.x, machine.prize.y

        a = (by * px - bx * py) / (by * ax - bx * ay)
        b = (px - ax * a) / bx

        if max_pressed is not None and (a > max_pressed or b > max_pressed):
            return 0

        tokens = 3 * a + b
        return round(tokens) if abs(round(tokens) - tokens) < 1e-10 else 0

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
