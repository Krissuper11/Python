"""Test ex08 part 2."""
import solution


def test_student_study_evening():
    """Test evening times in student study."""
    time_list = [18, 20, 24]
    for time in time_list:
        assert solution.students_study(time, True) is True
    for time in time_list:
        assert solution.students_study(time, False) is True


def test_student_study_night():
    """Test night times in student study."""
    time_list = [1, 3, 4]
    for time in time_list:
        assert solution.students_study(time, True) is False
    for time in time_list:
        assert solution.students_study(time, False) is False


def test_student_study_day():
    """Test day times in student study."""
    time_list = [5, 13, 17]
    for time in time_list:
        assert solution.students_study(time, True) is True
    for time in time_list:
        assert solution.students_study(time, False) is False


def test_student_study_zero_input():
    """Test time zero in student study."""
    assert solution.students_study(0, False) is False
    assert solution.students_study(0, True) is False


def test_lottery_big_win():
    """Test big win condition in lottery."""
    assert solution.lottery(5, 5, 5) == 10


def test_lottery_middle_win():
    """Test middle win condition in lottery."""
    assert solution.lottery(4, 4, 4) == 5


def test_lottery_middle_win_negative_num():
    """Test middle win with negative numbers."""
    assert solution.lottery(-2, -2, -2) == 5


def test_lottery_middle_win_zero():
    """Test middle win with negative numbers."""
    assert solution.lottery(0, 0, 0) == 5


def test_lottery_small_win():
    """Test small win condition in lottery."""
    assert solution.lottery(4, 3, 2) == 1
    assert solution.lottery(4, 3, 3) == 1


def test_lottery_no_win():
    """Test now in condition in lottery."""
    assert solution.lottery(2, 2, 1) == 0
    assert solution.lottery(1, 2, 1) == 0


def test_fruit_order_zero_amount():
    """Test zero input in fruit order."""
    assert solution.fruit_order(0, 0, 0) == 0
    assert solution.fruit_order(0, 2, 0) == 0
    assert solution.fruit_order(2, 0, 0) == 0
    assert solution.fruit_order(1, 2, 0) == 0


def test_fruit_order_exact_amount():
    """Test ideal amount of boxes for orders."""
    assert solution.fruit_order(4, 1, 9) == 4
    assert solution.fruit_order(5, 5, 30) == 5
    assert solution.fruit_order(1004, 20, 1104) == 1004
    assert solution.fruit_order(6, 0, 6)


def test_fruit_order_many_big_boxes():
    """Test too many big boxes."""
    assert solution.fruit_order(1, 8, 6) == 1
    assert solution.fruit_order(4, 17, 19) == 4
    assert solution.fruit_order(0, 2, 5) == 0


def test_fruit_order_many_small_boxes():
    """Test too many small boxes."""
    assert solution.fruit_order(15, 2, 16) == 6
    assert solution.fruit_order(27, 1, 31) == 26
    assert solution.fruit_order(5, 0, 5) == 5
    assert solution.fruit_order(7, 0, 4)


def test_fruit_order_many_boxes():
    """Test too many small and big boxes."""
    assert solution.fruit_order(15, 25, 9) == 4
    assert solution.fruit_order(4, 5, 2) == 2


def test_fruit_order_fail_not_enough_boxes():
    """Test wrong situation with result -1."""
    assert solution.fruit_order(1, 5, 18) == -1
    assert solution.fruit_order(1, 1, 7) == -1
    assert solution.fruit_order(0, 1, 6) == -1
    assert solution.fruit_order(10, 0, 11) == -1


def test_fruit_order_fail_many_big_boxes_no_small():
    """Test too many big boxes and no small boxes."""
    assert solution.fruit_order(0, 5, 4) == -1
    assert solution.fruit_order(0, 6, 9) == -1
    assert solution.fruit_order(0, 2, 25) == -1
    assert solution.fruit_order(1, 25, 10500)


# def test_fruit_order_negative():
#     """Test with negative numbers."""
#     assert solution.fruit_order(-1, 0, 5) == -1
#     assert solution.fruit_order(0, 0, -15) == 0
#     assert solution.fruit_order(1, -15, 1) == 1

