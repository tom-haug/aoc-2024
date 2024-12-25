from src.days.day17.a import Day17PartAController
from src.days.day17.b import Day17PartBController
from src.days.day17.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay17(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day17PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day17PartBController()
