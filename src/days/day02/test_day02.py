from src.days.day02.a import Day02PartAController
from src.days.day02.b import Day02PartBController
from src.days.day02.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay02(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day02PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day02PartBController()
