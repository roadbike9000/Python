from botCodeExamples.calculate_days_between_two_dates import days_between

import pytest


def test_days_between_same_day():
    d1 = '2024-03-12'
    d2 = '2024-03-12'
    assert days_between(d1, d2) == 0


def test_days_between_positive_days():
    d1 = '2024-03-12'
    d2 = '2024-03-27'
    assert days_between(d1, d2) == 15


def test_days_between_negative_days():
    d1 = '2024-03-27'
    d2 = '2024-03-12'
    assert days_between(d1, d2) == 15


def test_days_between_invalid_date():
    d1 = '2024-03-12'
    d2 = 'invalid_date'
    with pytest.raises(ValueError):
        days_between(d1, d2)
