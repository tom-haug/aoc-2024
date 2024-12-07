from src.days.day06.a import Day06PartAController
from src.days.day06.b import Day06PartBController
from src.days.day06.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay06(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day06PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day06PartBController()
