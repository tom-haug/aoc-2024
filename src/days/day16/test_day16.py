from src.days.day16.a import Day16PartAController
from src.days.day16.b import Day16PartBController
from src.days.day16.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay16(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day16PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day16PartBController()
