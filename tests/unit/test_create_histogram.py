""" from io import StringIO
from unittest.mock import patch """
from codingIntroduction.create_histogram import create_histogram


""" def test_mixed_valid_and_invalid_integers():
    user_input = "4 a 7"
    expected_output = "Sorry, some of the values are not integers. Please enter integers separated by spaces."

    with patch('builtins.input', return_value=user_input), patch('sys.stdout', new=StringIO()) as fake_output:
        create_histogram(user_input)
        assert fake_output.getvalue() == expected_output """


def test_create_histogram_with_non_integer_input():
    # Simulate non-integer input
    input_string = '3 5 a'
    expected_output = ["Sorry, some of the values are not integers. Please enter integers separated by spaces.\n"]

    # Call the create_histogram function with the simulated input and verify results
    result = create_histogram(input_string)
    assert result == expected_output


def test_valid_numbers():
    user_input = "3 5 2"
    expected_output = ["***", "*****", "**"]  # Expected histogram representation

    # Call the create_histogram function with the simulated input and verify results
    result = create_histogram(user_input)
    assert result == expected_output


def test_empty_input():
    user_input = ""  # Empty string
    expected_output = ["No input provided. Please enter a list of integers separated by spaces.\n"]

    result = create_histogram(user_input)
    assert result == expected_output
