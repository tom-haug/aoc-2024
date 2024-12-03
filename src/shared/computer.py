from __future__ import annotations
from enum import Enum


Registers = dict[str, int]


class InstructionType(Enum):
    UNKNOWN = 0
    NOOP = 1
    ADDX = 2

    @classmethod
    def parse(cls, input: str) -> InstructionType:
        match input:
            case "noop":
                return cls.NOOP
            case "addx":
                return cls.ADDX
            case _:
                return cls.UNKNOWN


class Instruction:
    type: InstructionType
    value: int

    def __init__(self, input: str):
        parts = input.split(" ")
        self.type = InstructionType.parse(parts[0])
        self.value = int(parts[1]) if len(parts) > 1 else 0


class Processor:
    registers: Registers

    def __init__(self, *register_keys: str):
        self.registers = {}
        for key in register_keys:
            self.registers[key] = 1

    def execute(self, instr: Instruction) -> int:
        match instr.type:
            case InstructionType.NOOP:
                return 1
            case InstructionType.ADDX:
                self.registers["X"] += instr.value
                return 2
            case _:
                return 0
