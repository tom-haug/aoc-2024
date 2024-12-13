from src.days.day11.a import Day11PartAController
from src.days.day11.b import Day11PartBController
from src.days.day11.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay11(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day11PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day11PartBController()
