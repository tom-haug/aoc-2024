from src.days.day12.a import Day12PartAController
from src.days.day12.b import Day12PartBController
from src.days.day12.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay12(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day12PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day12PartBController()
