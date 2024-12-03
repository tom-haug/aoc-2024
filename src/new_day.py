import argparse
from src.code_gen.create_day import create_day


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Helper to bootstrap files for problems"
    )
    parser.add_argument("day", type=int, help="Day to create files for")

    return parser


if __name__ == "__main__":
    args = create_parser().parse_args()
    create_day(args.day)
