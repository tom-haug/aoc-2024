from src.days.day15.a import Day15PartAController
from src.days.day15.b import Day15PartBController
from src.days.day15.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay15(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day15PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day15PartBController()
