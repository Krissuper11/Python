"""Test ex04."""
import solution


def test_part1_int_correct_len():
    """Test correct length in part 1."""
    element_list = ["string", "int", "float", "list", "tuple", "dict", "set"]
    counter = 2
    for element in element_list:
        res = solution.generate_list(counter, element)
        assert len(res) == counter
        counter += 1


def test_part1_zero():
    """Test zero input in part 1."""
    input_amount = 0
    res = solution.generate_list(input_amount, "string")
    expected_len = 0
    assert len(res) == expected_len


def test_part1_correct_data_type():
    """Test if all elements of list are same types in part 1."""
    element_list = ["string", "int", "float", "list", "tuple", "dict", "set"]
    datatype_list = [str, int, float, list, tuple, dict, set]
    for i, data_type in enumerate(datatype_list):
        output_list = solution.generate_list(4, element_list[i])
        for element in output_list:
            assert isinstance(element, data_type)


def test_part1_big_number():
    """Test for too large number in test 1."""
    input_amount = 1000
    res = solution.generate_list(input_amount, "string")
    expected_len = 1000
    assert len(res) == expected_len


def test_part2_correct_len():
    """Test correct length in part 2."""
    element_list = ["string", "int", "float", "list", "tuple", "dict", "set"]
    input_min = 1
    input_max = 2
    for element in element_list:
        assert len(solution.generate_combined_list([(input_min, element), (input_max, element)])) == input_max
        input_min += 1
        input_max += 1


def test_part2_correct_data_type_single():
    """Test if all elements of list are same types in part 2."""
    element_list = ["string", "int", "float", "list", "tuple", "dict", "set"]
    datatype_list = [str, int, float, list, tuple, dict, set]
    for i, data_type in enumerate(datatype_list):
        output_list = solution.generate_combined_list([(4, element_list[i])])
        for element in output_list:
            assert isinstance(element, data_type)


def test_part2_big_number():
    """Test for too large number in test 2."""
    input_amount = 1000
    res = solution.generate_combined_list([(input_amount, "string")])
    expected_len = 1000
    assert len(res) == expected_len


def test_part3_correct_len():
    """Test correct length in part 3."""
    element_list = ["string", "int", "float"]
    input_min = 0
    input_max = 0
    for element in element_list:
        assert len(solution.generate_combined_list_unique([(input_min, element), (input_max, element)])) == input_max
        input_min += 1
        input_max += 2


def test_part3_correct_data_type_single():
    """Test if all elements of list are same types in part 3."""
    element_list = ["string", "int", "float"]
    datatype_list = [str, int, float]
    for i, data_type in enumerate(datatype_list):
        output_list = solution.generate_combined_list_unique([(4, element_list[i])])
        for element in output_list:
            assert isinstance(element, data_type)


def test_part3_unique_single():
    """Test if all elements of list are unique in part 3."""
    element_list = ["string", "int", "float"]
    for data_type in element_list:
        output_list = solution.generate_combined_list_unique([(4, data_type)])
        for i in range(1, len(output_list)):
            assert output_list[i] != output_list[i - 1]


def test_part3_big_number():
    """Test for too large number in test 3."""
    input_amount = 1000
    res = solution.generate_combined_list_unique([(input_amount, "string")])
    expected_len = 1000
    assert len(res) == expected_len
