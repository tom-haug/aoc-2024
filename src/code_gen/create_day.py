import aocd
import os
from src.code_gen.file_data import FileData
from src.code_gen.templates.part_template import PART_TEMPLATE
from src.code_gen.templates.solver_template import SOLVER_TEMPLATE
from src.code_gen.templates.test_template import TEST_TEMPLATE
from src.shared.file_loading import touch_file, write_file
from src.shared.variables import AOC_TOKEN, AOC_YEAR


def create_files(year: int, file_data: FileData) -> None:
    if not os.path.isdir(file_data.directory):
        os.makedirs(file_data.directory)
        os.makedirs(file_data.input_directory)
        touch_file(file_data.src_init_file)
        write_file(
            file_data.input_file,
            aocd.get_data(session=AOC_TOKEN, year=year, day=file_data.day),
        )
        write_file(
            file_data.solver_file,
            SOLVER_TEMPLATE.format(day_string=file_data.day_string),
        )
        write_file(
            file_data.test_file, TEST_TEMPLATE.format(day_string=file_data.day_string)
        )
        for part in ["a", "b"]:
            file_data.part = part
            write_file(
                file_data.part_file,
                PART_TEMPLATE.format(
                    year=year,
                    day_int=int(file_data.day_string),
                    day_string=file_data.day_string,
                    part=part,
                    part_upper=part.upper(),
                ),
            )


def create_day(day: int):
    file_data = FileData(day=day, part="a")
    create_files(AOC_YEAR, file_data)
