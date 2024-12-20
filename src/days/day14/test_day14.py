from src.days.day14.a import Day14PartAController
from src.days.day14.b import Day14PartBController
from src.days.day14.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay14(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day14PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day14PartBController()
