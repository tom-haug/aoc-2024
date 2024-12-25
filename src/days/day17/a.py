from src.shared.controller import Controller
from src.days.day17.solver import AnswerType, Day17Solver, OpCodeType
from src.shared.file_result import FileResult


class Day17PartASolver(Day17Solver):
    def solve(self) -> AnswerType:
        instr_pointer = 0
        while True:
            if instr_pointer >= len(self.program) - 1:
                break
            opcode = OpCodeType(self.program[instr_pointer])
            operand = self.program[instr_pointer + 1]
            instr_pointer = self._perform_instruction(opcode, operand, instr_pointer)
        return ",".join(str(x) for x in self.output)

    def _get_combo_input(self, operand: int) -> int:
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.register_a
            case 5:
                return self.register_b
            case 6:
                return self.register_c
            case 7 | _:
                raise ValueError("Invalid operand")

    def _perform_instruction(
        self, opcode: OpCodeType, operand: int, instr_pointer: int
    ) -> int:
        if self.show_visual:
            print(
                f"InsrPointer: {instr_pointer}, RegA: {self.register_a}, RegB: {self.register_b}, RegC: {self.register_c}, OpCode: {opcode.name}, Operand: {operand}"
            )
        match opcode:
            case OpCodeType.ADV:
                numerator = self.register_a
                denominator = 2 ** self._get_combo_input(operand)
                self.register_a = numerator // denominator
                return instr_pointer + 2
            case OpCodeType.BXL:
                self.register_b ^= operand
                return instr_pointer + 2
            case OpCodeType.BST:
                self.register_b = self._get_combo_input(operand) % 8
                return instr_pointer + 2
            case OpCodeType.JNZ:
                return operand if self.register_a != 0 else instr_pointer + 2
            case OpCodeType.BXC:
                self.register_b ^= self.register_c
                return instr_pointer + 2
            case OpCodeType.OUT:
                self.output.append(self._get_combo_input(operand) % 8)
                if self.show_visual:
                    print(self._get_combo_input(operand) % 8, ",")
                return instr_pointer + 2
            case OpCodeType.BDV:
                numerator = self.register_a
                denominator = 2 ** self._get_combo_input(operand)
                self.register_b = numerator // denominator
                return instr_pointer + 2
            case OpCodeType.CDV:
                numerator = self.register_a
                denominator = 2 ** self._get_combo_input(operand)
                self.register_c = numerator // denominator
                return instr_pointer + 2
            case _:
                raise ValueError("Invalid opcode")


class Day17PartAController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(17, "a")

    def _new_solver(self):
        return Day17PartASolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", "4,6,3,5,6,3,5,2,1,0")]


if __name__ == "__main__":
    controller = Day17PartAController()
    controller.run()
