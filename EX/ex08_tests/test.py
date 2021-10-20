import pytest
import solution


def test_part1_int_correct_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len


def test_part1_zero():
    input_amount = 0
    res = solution.generate_list(input_amount, "string")
    expected_len = 0
    assert len(res) == expected_len


def test_part1_correct_data_type():
    element_list = ["string", "int", "float", "list", "tuple", "dict", "set"]
    datatype_list = [str, int, float, list, tuple, dict, set]
    for i, element in enumerate(datatype_list):
        output_list = solution.generate_list(4, element_list[i])
        for datatype in output_list:
            assert isinstance(datatype, element)


def test_part2_correct_len():
    element_list = ["string", "int", "float", "list", "tuple", "dict", "set"]
    counter = 0
    counter_max = 0
    for element in element_list:
        input_min = counter
        input_max = counter_max
        assert len(solution.generate_combined_list([(input_min, element), (input_max, element)])) == input_max
        counter += 1
        counter_max += 2


def test_part2_correct_data_type_single():
    element_list = ["string", "int", "float", "list", "tuple", "dict", "set"]
    datatype_list = [str, int, float, list, tuple, dict, set]
    for i, element in enumerate(datatype_list):
        output_list = solution.generate_combined_list([(4, element_list[i])])
        for datatype in output_list:
            assert isinstance(datatype, element)
