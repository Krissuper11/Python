"""Test ex08 part 2."""
import pytest
import solution


# def test_student_study_evening():
#     """Test evening times in student study."""
#     time_list = [18, 20, 24]
#     for time in time_list:
#         assert solution.students_study(time, True) is True
#     for time in time_list:
#         assert solution.students_study(time, False) is True
#
#
# def test_student_study_night():
#     """Test night times in student study."""
#     time_list = [1, 3, 4]
#     for time in time_list:
#         assert solution.students_study(time, True) is False
#     for time in time_list:
#         assert solution.students_study(time, False) is True
#
#
# def test_student_study_day():
#     """Test day times in student study."""
#     time_list = [5, 13, 17]
#     for time in time_list:
#         assert solution.students_study(time, True) is True
#     for time in time_list:
#         assert solution.students_study(time, False) is False
#
#
# def test_student_study_zero_input():
#     """Test time zero in student study."""
#     assert solution.students_study(0, False) is False
#     assert solution.students_study(0, True) is False


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
