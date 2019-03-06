import pytest
from fizz_buzz_python.roman_numerals_calculator import (
    get_number_for_roman_numeral,
    convert_roman_numeral_to_number,
    roman_numeral_calculator,
)


@pytest.mark.parametrize("numeral,num,is_valid", [
    ('I', 1, True),
    ('V', 5, True),
    ('X', 10, True),
    ('L', 50, True),
    ('C', 100, True),
    ('D', 500, True),
    ('M', 1000, True),
    ('A', 0, False),
    ('B', 0, False),
    ('Z', 0, False),
])
def test_get_number_for_roman_numeral(numeral, num, is_valid):
    if is_valid:
        assert get_number_for_roman_numeral(numeral) == num
    else:
        with pytest.raises(ValueError) as e:
            get_number_for_roman_numeral(numeral)
            assert str(e) == 'Digit is not a valid roman numeral'


@pytest.mark.parametrize('numeral_str,num,is_valid', [
    ('I', 1, True),
    ('V', 5, True),
    ('X', 10, True),
    ('L', 50, True),
    ('C', 100, True),
    ('D', 500, True),
    ('M', 1000, True),
    ('II', 2, True),
    ('III', 3, True),
    ('IV', 4, True),
    ('VI', 6, True),
    ('IX', 9, True),
    ('CM', 900, True),
    ('XL', 40, True),
    ('XXIV', 24, True),
])
def test_convert_roman_numeral_to_number(numeral_str, num, is_valid):
    if is_valid:
        assert convert_roman_numeral_to_number(numeral_str) == num
    else:
        with pytest.raises(ValueError) as e:
            convert_roman_numeral_to_number(numeral_str)
            assert str(e) == 'Not a valid numeral string'


@pytest.mark.parametrize('numeral_str,num,is_valid', [
    ('I + I', 2, True),
    ('V - I', 4, True),
    ('V - III', 2, True),
    ('I - X', -9, True),
    ('II^II - IV', 0, True),
])
def test_roman_numeral_calculator(numeral_str, num, is_valid):
    if is_valid:
        assert roman_numeral_calculator(numeral_str) == num
    else:
        with pytest.raises(ValueError) as e:
            roman_numeral_calculator(numeral_str)
            assert str(e) == 'Unable to calculate value'
