"""Test ex08 part 2."""
import pytest
import solution


def test_student_study_evening():
    """Test evening times in student study."""
    time_list = [18, 20, 24]
    for time in time_list:
        res = solution.students_study(time, True)
        assert res is True
    for time in time_list:
        res = solution.students_study(time, False)
        assert res is True


def test_student_study_night():
    """Test night times in student study."""
    time_list = [1, 3, 4]
    for time in time_list:
        res = solution.students_study(time, True)
        assert res is False
    for time in time_list:
        res = solution.students_study(time, False)
        assert res is True


def test_student_study_day():
    """Test day times in student study."""
    time_list = [5, 13, 17]
    for time in time_list:
        res = solution.students_study(time, True)
        assert res is True
    for time in time_list:
        res = solution.students_study(time, False)
        assert res is False


def test_student_study_zero_input():
    """Test time zero in student study."""
    res = solution.students_study(0, False)
    assert res is False
    res = solution.students_study(0, True)
    assert res is False
