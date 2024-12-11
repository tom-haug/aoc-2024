from src.days.day10.a import Day10PartAController
from src.days.day10.b import Day10PartBController
from src.days.day10.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay10(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day10PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day10PartBController()
