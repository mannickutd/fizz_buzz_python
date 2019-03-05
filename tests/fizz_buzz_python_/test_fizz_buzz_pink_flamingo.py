import pytest
from fizz_buzz_python.fizz_buzz_pink_flamingo import is_fizz_buzz_number


@pytest.mark.parametrize("num,expected_str", [
    (0, '0'),
    (2, '2'),
    (3, 'Fizz'),
    (4, '4'),
    (5, 'Buzz'),
    (-1, '-1'),
    (8, '8'),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (15, 'FizzBuzz'),
])
def test_is_fizz_buzz_number(num, expected_str):
	assert is_fizz_buzz_number(num) == expected_str