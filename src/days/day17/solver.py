from abc import abstractmethod
from enum import Enum
from typing import NamedTuple
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file


AnswerType = str


class OpCodeType(Enum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


class Instruction(NamedTuple):
    opcode: OpCodeType
    operand: int


class Day17Solver(Solver[AnswerType]):
    register_a: int
    register_b: int
    register_c: int
    program: list[int]
    output: list[int]
    # instructions: list[Instruction]

    def initialize(self, file_path: str):
        input = load_text_file(file_path) or ""
        registers_section, program_section = input.split("\n\n")
        registers = registers_section.split("\n")
        self.register_a = int(registers[0].split(": ")[1])
        self.register_b = int(registers[1].split(": ")[1])
        self.register_c = int(registers[2].split(": ")[1])
        self.program = [int(char) for char in program_section.split(": ")[1].split(",")]
        self.output = []

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
