from src.days.day08.a import Day08PartAController
from src.days.day08.b import Day08PartBController
from src.days.day08.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay08(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day08PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day08PartBController()
