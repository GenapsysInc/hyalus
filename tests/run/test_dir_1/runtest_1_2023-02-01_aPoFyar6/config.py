"""This test run dir is here to assert that output test run directories are ignored during relevant processing"""
# pylint: disable=import-outside-toplevel

__author__ = "David McConnell"
__credits__ = ["David McConnell"]
__created_on__ = "2022-10-22"

from hyalus.config.steps import RunFunctionStep, AssertEQ
from hyalus.config.tags import Short, FunctionalTest

TEST_DESCRIPTION = "Runs a function and a few assertions"
INPUT_DATA = "N/A, no input data"


def custom_func(json_file, to_dump):
    import json

    with open(json_file, 'w', encoding='utf-8') as fh:
        json.dump(to_dump, fh)


STEPS = [
    RunFunctionStep(custom_func, "output/food.json", {"best_cuisine": "Mexican"}),
    RunFunctionStep(custom_func, "output/coffee.json", {"best_coffee_shop": "Ozo"}),
    AssertEQ(("output/food.json", ["best_cuisine"]), "Mexican"),
    AssertEQ(("output/coffee.json", ["best_coffee_shop"]), "Ozo"),
]

TAGS = [Short(info="Should run in seconds"), FunctionalTest()]
