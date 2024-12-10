from dataclasses import dataclass
from src.shared.controller import Controller
from src.days.day09.solver import AnswerType, Day09Solver
from src.shared.file_loading import load_text_file
from src.shared.file_result import FileResult


@dataclass
class FileData:
    id: int
    size: int
    position: int


class Day09PartBSolver(Day09Solver):
    gaps: list[FileData]
    files: list[FileData]

    def initialize(self, file_path: str):
        input = load_text_file(file_path) or ""
        self.gaps = []
        self.files = []
        position = 0
        for idx, char in enumerate(input):
            file_length = int(char)
            is_file = idx % 2 == 0
            file_id = int(idx / 2) if is_file else 0

            file_data = FileData(file_id, file_length, position)
            if is_file:
                self.files.append(file_data)
            else:
                self.gaps.append(file_data)
            position += file_length

    def solve(self) -> AnswerType:
        compacted: dict[int, FileData] = {}

        while len(self.files) > 0:
            file = self.files.pop()
            was_written = False
            for gap in self.gaps:
                if gap.position > file.position:
                    break
                if gap.size >= file.size:
                    was_written = True
                    compacted[gap.position] = file
                    gap.size -= file.size
                    gap.position += file.size
                    break
            if not was_written:
                compacted[file.position] = file

        return self._calculate_checksum(compacted)

    def _calculate_checksum(self, data: dict[int, FileData]) -> int:
        total = 0
        for start_idx, file in data.items():
            for idx in range(start_idx, start_idx + file.size):
                total += idx * file.id
        return total


class Day09PartBController(Controller[AnswerType]):
    def __init__(self):
        super().__init__(9, "b")

    def _new_solver(self):
        return Day09PartBSolver()

    def _to_answer_type(self, value: str) -> AnswerType:
        return AnswerType(value)

    def test_inputs(self) -> list[FileResult[AnswerType]]:
        return [FileResult("sample01.txt", 2858)]


if __name__ == "__main__":
    controller = Day09PartBController()
    controller.run()
