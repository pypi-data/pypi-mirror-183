#!/usr/bin/python3
import argparse
import random
from pathlib import Path
from typing import NoReturn

from pddl_plus_parser.problem_generators import get_problem_template

TEMPLATE_FILE_PATH = Path("counters_template.pddl")


def generate_instance(instance_name: str, num_counters: int, max_int: int) -> str:
    """Generate a single planning problem instance.

    :param instance_name: the name of the problem instance.
    :param num_counters: the number of counters in the problem.
    :param max_int: the maximal integer value.
    :return: the string representing the planning problem.
    """
    template = get_problem_template(TEMPLATE_FILE_PATH)
    template_mapping = {
        "instance_name": instance_name,
        "domain_name": "fo-counters-rnd",
        "counters_list": " ".join([f"c{i}" for i in range(num_counters)]),
        "counters_initial_values": "\n\t".join(
            [f"(= (value c{i}) {random.randint(0, max_int)})" for i in range(num_counters)]),
        "counters_rate_values": "\n\t".join([f"(= (rate_value c{i}) 0)" for i in range(num_counters)]),
        "max_int_value": max_int,
        "counters_final_values": "\n\t".join(
            [f"(<= (+ (value c{i}) 1) (value c{i + 1}))" for i in range(num_counters - 1)])
    }
    return template.substitute(template_mapping)


def parse_arguments() -> argparse.Namespace:
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser(description="Generate counters planning instance")
    parser.add_argument("--min_counters", required=True, help="Minimal number of counters in the problems")
    parser.add_argument("--max_counters", required=True, help="Maximal number of counters in the problems")
    parser.add_argument("--max_int", required=True, help="Maximal integer value")
    parser.add_argument("--output_path", required=True,
                        help="The path to the output folder where the problems will be saved")
    args = parser.parse_args()
    return args


def generate_multiple_problems(
        min_counters: int, max_counters: int, max_int: int, output_folder: Path) -> NoReturn:
    """Generate multiple problems based on the input arguments.

    :param min_counters: the minimal number of counters possible in the problems.
    :param max_counters: the maximal number of counters possible in the problems.
    :param max_int: the maximal integer value.
    :param output_folder: the path to the output folder where the problems will be saved.
    """
    counters_range = [i for i in range(min_counters, max_counters + 1)]
    for num_counters in counters_range:
        print(f"Generating problem with {num_counters} counters")
        with open(output_folder / f"pfile{num_counters}_{random.randint(0, 100)}.pddl", "wt") as problem_file:
            problem_file.write(
                generate_instance(f"instance_{num_counters}_{max_int}", num_counters, max_int))


def main():
    args = parse_arguments()
    generate_multiple_problems(min_counters=int(args.min_counters),
                               max_counters=int(args.max_counters),
                               max_int=int(args.max_int),
                               output_folder=Path(args.output_path))


if __name__ == '__main__':
    main()
