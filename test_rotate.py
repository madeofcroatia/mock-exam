"""
Test code for Cyclic Rotations

Sardor Gulyamov 2022
"""

import json
import os
import sys

import pytest

import rotate

# Handle the fact that the grading code may not
# be in the same directory as rotate.py
sys.path.append(os.getcwd())

# Get the name of the directory that holds the grading code.
BASE_DIR = os.path.dirname(__file__)
TEST_DIR = os.path.join(BASE_DIR, "tests")


def read_config_file(filename):
    """
    Load the test cases from a JSON file.

    Inputs:
      filename (string): the name of the test configuration file.

    Returns: (list) test cases
    """

    with open(os.path.join(TEST_DIR, filename)) as f:
        return json.load(f)


def gen_none_error(recreate_msg):
    """
    Generate the error message for an unexpected return value of None.

    Inputs:
      recreate_msg (string): a string with the information needed to
        rerun the test in ipython.

    Returns (string): error message
    """

    msg = "The function returned None."
    msg += " Did you forget to include a return statement?\n"
    return msg + recreate_msg + "\n"


def gen_type_error(recreate_msg, expected, actual):
    """
    Generate the error message for a return value of the wrong type

    Inputs:
      recreate_msg (string): a string with the information needed to
        rerun the test in ipython.

    Returns (string): error message
    """

    msg = "The function returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n"
    msg += "  Actual return type: {}.\n"
    msg += recreate_msg + "\n"
    return msg.format(type(expected), type(actual))


def gen_mismatch_error(recreate_msg, expected, actual):
    """
    Generate the error message for the case whether the expected and
    actual values do not match.

    Inputs:
      recreate_msg (string): a string with the information needed to
        rerun the test in ipython.

    Returns (string): error message
    """

    msg = "Actual ({}) and expected ({}) values do not match.\n"
    msg += recreate_msg + "\n"
    return msg.format(actual, expected)


# Task: Count number of infected people ######

@pytest.mark.parametrize(
    "params",
    read_config_file("rotate_by_1.json"))
def test_rotate_right_by_1(params):
    """
    Test harness for count_infected function.

    Inputs:
      params (dictionary): the test parameters:
        city and the expected number of infected folks in the city.
    """

    actual_array = rotate.rotate_right_by_1(params["array"])

    recreate_msg = "To recreate this test in python3 run:\n"
    recreate_msg += f'  rotate.rotate_right_by_1({params["city"]})'

    assert actual_array is not None, \
        gen_none_error(recreate_msg)

    expected_array = params["expected"]
    assert isinstance(actual_array, type(expected_array)), \
        gen_type_error(recreate_msg,
                       expected_array,
                       actual_array)

    assert actual_array == expected_array, \
        gen_mismatch_error(recreate_msg,
                           expected_array,
                           actual_array)


# Task: has_an_infected_neighbor

@pytest.mark.parametrize(
    "params",
    read_config_file("rotate_by_1.json"))
def test_rotate_right_by_1(params):
    """
    Test harness for rotate_right_by_1 function.

    Inputs:
      params (dictionary): the test parameters:
        array and expected array after rotating cyclically array by 1 to right.
    """

    actual_array = rotate.rotate_right_by_1(params["array"])

    recreate_msg = "To recreate this test in python3 run:\n"
    recreate_msg += f'  rotate.rotate_right_by_1({params["array"]})'

    assert actual_array is not None, \
        gen_none_error(recreate_msg)

    expected_array = params["expected"]
    assert isinstance(actual_array, type(expected_array)), \
        gen_type_error(recreate_msg,
                       expected_array,
                       actual_array)

    assert actual_array == expected_array, \
        gen_mismatch_error(recreate_msg,
                           expected_array,
                           actual_array)


@pytest.mark.parametrize(
    "params",
    read_config_file("rotate_right_by_k.json"))
def test_rotate_right_by_k(params):
    """
    Test harness for rotate_right_by_k function.

    Inputs:
      params (dictionary): the test parameters:
        array, k, and the expected array
    """

    actual_array = rotate.rotate_right_by_k(params["array"], params["k"])

    recreate_msg = "To recreate this test in python3 run:\n" \
                   f'  rotate.rotate_right_by_k({params["array"]}, {params["k"]})'

    assert actual_array is not None, \
        gen_none_error(recreate_msg)

    expected_array = params["expected"]
    assert isinstance(actual_array, type(expected_array)), \
        gen_type_error(recreate_msg,
                       expected_array,
                       actual_array)

    assert actual_array == expected_array, \
        gen_mismatch_error(recreate_msg,
                           expected_array,
                           actual_array)


@pytest.mark.parametrize(
    "params",
    read_config_file("rotate_by_k.json"))
def test_rotate_by_k(params):
    """
    Test harness for rotate_by_k function.

    Inputs:
      params (dictionary): the test parameters:
        array, k, and the expected array
    """

    actual_array = rotate.rotate_by_k(params["array"], params["k"])

    recreate_msg = "To recreate this test in python3 run:\n" \
                   f'  rotate.rotate_by_k({params["array"]}, {params["k"]})'

    assert actual_array is not None, \
        gen_none_error(recreate_msg)

    expected_array = params["expected"]
    assert isinstance(actual_array, type(expected_array)), \
        gen_type_error(recreate_msg,
                       expected_array,
                       actual_array)

    assert actual_array == expected_array, \
        gen_mismatch_error(recreate_msg,
                           expected_array,
                           actual_array)