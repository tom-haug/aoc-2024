from src.days.day05.a import Day05PartAController
from src.days.day05.b import Day05PartBController
from src.days.day05.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay05(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day05PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day05PartBController()
