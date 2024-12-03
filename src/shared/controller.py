import argparse
import inspect
import os
from abc import ABC, abstractmethod
import time
from aocd.models import Puzzle
from typing import Any, Generic, TypeVar
from src.shared.extra_params import ExtraParams
from src.shared.file_loading import load_text_file, touch_file, write_file
from src.shared.print_helpers import Colors
from src.shared.solver import Solver
from src.shared.file_result import FileResult
from src.shared.variables import AOC_YEAR

T = TypeVar("T")


class Controller(ABC, Generic[T]):
    day: int
    part: str
    args: argparse.Namespace

    def __init__(self, day: int, part: str):
        self.day = day
        self.part = part
        self.args = create_parser().parse_known_args()[0]

    @property
    def day_path(self) -> str:
        return os.path.dirname(inspect.getfile(self.__class__))

    @property
    def input_path(self) -> str:
        return os.path.join(self.day_path, "inputs")

    def run(self) -> None:
        self.__run_test_inputs()
        self.__run_main_input()

    def main_input(self) -> FileResult[T]:
        input_path = "main.txt"
        answer_path = os.path.join(self.input_path, f"{self.part}_answer.txt")
        answer = load_text_file(answer_path)
        result = None if answer is None else self._to_answer_type(answer)
        extra_params = self._main_input_extra_params()
        return FileResult(input_path, result, extra_params)

    @abstractmethod
    def test_inputs(self) -> list[FileResult[T]]:
        ...

    def _main_input_extra_params(self) -> dict[str, Any]:
        return {}

    # def solve(self, file_name: str, extra_params: dict[str, Any] = {}) -> T:
    def solve(self, test: FileResult[T]) -> T:

        if (
            test.expected_result
            and ExtraParams.LongRunning in test.extra_params
            and not self.args.force
        ):
            print(f"{Colors.WARNING}Long-running solve. Execution overridden.")
            return test.expected_result

        file_path = os.path.join(self.input_path, test.file_path)
        solver = self._new_solver()
        solver.initialize_extra_params(test.extra_params)
        solver.initialize(file_path)

        start = time.time()
        result = solver.solve()
        end = time.time()
        print(f"{Colors.OKBLUE}elapsed: {(end - start) * 1000}ms")
        return result

    @abstractmethod
    def _new_solver(self) -> Solver[T]:
        ...

    @abstractmethod
    def _to_answer_type(self, value: str) -> T:
        ...

    def __run_test_inputs(self) -> None:
        tests = self.test_inputs()
        if len(tests) == 0:
            raise Exception(
                f"No test files setup. Add these to: {self.__class__.__name__}"
            )
        for test in tests:
            self.__run_input(test)

    def __run_main_input(self) -> None:
        self.__run_input(self.main_input())

    def __run_input(self, test_pair: FileResult[T]) -> None:
        file_path = test_pair.file_path
        expected_result = test_pair.expected_result

        test_pair.extra_params[ExtraParams.ShowVisual] = self.args.visual

        result = self.solve(test_pair)
        if expected_result is None:
            print(f"Result: File: {file_path}, result: {result}")
            self.__try_submit(result)
        else:
            if result != expected_result:
                raise Exception(
                    f"{Colors.FAIL}Test Failed: File: {file_path}, expecting: {expected_result}, actual: {result}"
                )
            print(f"{Colors.OKGREEN}Test Passed: File: {file_path}, result: {result}")

    def __try_submit(self, answer: T):
        dryrun = self.args.dryrun
        if not dryrun:
            puzzle = Puzzle(year=AOC_YEAR, day=self.day)
            if self.part == "a":
                puzzle.answer_a = answer
                if puzzle.answer_a is not None:
                    self.__update_main_result(answer)
            else:
                puzzle.answer_b = answer
                if puzzle.answer_b is not None:
                    self.__update_main_result(answer)

    def __update_main_result(self, result: T):
        controller_file_path = inspect.getfile(self.__class__)
        dir = os.path.dirname(controller_file_path)
        output_file = os.path.join(dir, "inputs", f"{self.part}_answer.txt")
        touch_file(output_file)
        write_file(output_file, str(result))


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Helper to bootstrap files for problems"
    )
    parser.add_argument(
        "-d", "--dryrun", action="store_true", help="Do NOT attempt to submit"
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Force execution of long-running solutions",
    )
    parser.add_argument(
        "-v",
        "--visual",
        action="store_true",
        help="Output solution visualization if available (will run slower)",
    )
    return parser
