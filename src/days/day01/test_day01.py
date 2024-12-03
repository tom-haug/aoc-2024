from src.days.day01.a import Day01PartAController
from src.days.day01.b import Day01PartBController
from src.days.day01.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay01(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day01PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day01PartBController()
