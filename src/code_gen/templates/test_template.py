TEST_TEMPLATE = """
from src.days.day{day_string}.a import Day{day_string}PartAController
from src.days.day{day_string}.b import Day{day_string}PartBController
from src.days.day{day_string}.solver import AnswerType
from src.shared.base_test import BaseTest
from src.shared.controller import Controller


class TestDay{day_string}(BaseTest[AnswerType]):
    def _get_controller_a(self) -> Controller[AnswerType]:
        return Day{day_string}PartAController()

    def _get_controller_b(self) -> Controller[AnswerType]:
        return Day{day_string}PartBController()
"""
