from src.days.day04.a import Day04PartAController
from src.days.day04.b import Day04PartBController
from src.days.day04.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay04(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day04PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day04PartBController()
