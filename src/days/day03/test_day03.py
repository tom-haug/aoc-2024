from src.days.day03.a import Day03PartAController
from src.days.day03.b import Day03PartBController
from src.days.day03.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay03(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day03PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day03PartBController()
