import pytest
import solution


def test_part1_int_correct_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len


def test_part2_correct_len():
    element_list = ["string", "int", "float", "list", "tuple", "dict", "set"]
    counter = 0
    for element in element_list:
        input_min = counter
        input_max = counter + 1
        assert input_max == len(solution.generate_combined_list([(input_min, element), (input_max, element)]))
        counter += 1


def test_correct_data_type_single():
    element_list = ["string", "int", "float", "list", "tuple", "dict", "set"]
    datatype_list = ["", 0, 0.1, [], (), {}, set()]
    for i, element in enumerate(element_list):
        output_list = solution.generate_combined_list([(4, element)])
        for datatype in output_list:
            assert type(datatype_list[i]) == type(datatype)
