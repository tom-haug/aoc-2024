from src.days.day07.a import Day07PartAController
from src.days.day07.b import Day07PartBController
from src.days.day07.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay07(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day07PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day07PartBController()
