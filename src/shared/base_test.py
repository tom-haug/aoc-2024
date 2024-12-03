from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from src.shared.controller import Controller, ExtraParams


T = TypeVar("T")


class BaseTest(ABC, Generic[T]):
    def test_part_a(self):
        controller = self._get_controller_a()
        self.__test_part(controller)

    def test_part_b(self):
        controller = self._get_controller_b()
        self.__test_part(controller)

    @abstractmethod
    def _get_controller_a(self) -> Controller[T]:
        ...

    @abstractmethod
    def _get_controller_b(self) -> Controller[T]:
        ...

    def __test_part(self, controller: Controller[T]):
        tests = controller.test_inputs()
        main_input = controller.main_input()
        if main_input.expected_result is not None:
            tests.append(main_input)

        assert len(tests) > 0
        print("\n")
        for test in tests:
            print(f"Runnning: {test}")
            test.extra_params[ExtraParams.ShowVisual] = False
            result = controller.solve(test)
            assert result == test.expected_result
