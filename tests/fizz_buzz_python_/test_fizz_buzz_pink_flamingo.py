import pytest
from fizz_buzz_python.fizz_buzz_pink_flamingo import (
	is_fizz_buzz_number,
	is_fibonacci,
	is_perfect_square,
)


@pytest.mark.parametrize("num,is_perfect_square_", [
	(2, False),
	(3, False),
])
def test_is_perfect_square_sanity(num, is_perfect_square_):
	assert is_perfect_square(num) == is_perfect_square_


@pytest.mark.parametrize("num,is_fib_", [
    (0, True),
    (1, True),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (7, False),
    (8, True),
    (9, False),
    (10, False),
    (13, True),
    (15, False),
    (6765, True),
])
def test_is_fibonacci(num, is_fib_):
	assert is_fibonacci(num) == is_fib_


@pytest.mark.parametrize("num,expected_str", [
    (0, '0'),
    (2, 'Flamingo'),
    (3, 'Fizz'),
    (4, '4'),
    (5, 'Buzz'),
    (-1, '-1'),
    (7, '7'),
    (8, 'Flamingo'),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (15, 'FizzBuzz'),
    (6765, 'Pink Flamingo'),
])
def test_is_fizz_buzz_number(num, expected_str):
	assert is_fizz_buzz_number(num) == expected_str