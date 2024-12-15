from src.days.day13.a import Day13PartAController
from src.days.day13.b import Day13PartBController
from src.days.day13.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay13(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day13PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day13PartBController()
