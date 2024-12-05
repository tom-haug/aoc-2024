from abc import abstractmethod

from nptyping import NDArray
import numpy as np
from src.shared.controller import Solver
from src.shared.file_loading import load_text_file_lines


AnswerType = int


class Day04Solver(Solver[AnswerType]):
    data: NDArray

    def initialize(self, file_path: str):
        input = load_text_file_lines(file_path) or ""
        self.data = np.array([list(line) for line in input])

    @abstractmethod
    def solve(self) -> AnswerType:
        ...
