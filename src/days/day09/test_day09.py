from src.days.day09.a import Day09PartAController
from src.days.day09.b import Day09PartBController
from src.days.day09.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay09(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day09PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day09PartBController()
