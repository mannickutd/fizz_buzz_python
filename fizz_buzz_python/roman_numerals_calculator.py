import re

CONVERSION_TABLE = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}


def get_number_for_roman_numeral(digit:str) -> int:
	if digit in CONVERSION_TABLE:
		return CONVERSION_TABLE[digit]
	else:
		raise ValueError("Digit is not a valid roman numeral")


def convert_roman_numeral_to_number(roman_numeral:str) -> int:
	total = 0
	num_list = []
	try:
		for dig in list(roman_numeral):
			num = get_number_for_roman_numeral(dig)
			num_list.append(num)
		len_num = len(num_list)
		for i, num in enumerate(num_list):
			if i+1 < len_num and num_list[i + 1] > num:
				total -= num
			else:
				total += num
		return total
	except ValueError:
		raise ValueError('Not a valid numeral string')


OPERATOR_LIST = ['(', ')', '+', '-', '*', '^', '/', ' ']


def roman_numeral_calculator(roman_str:str) -> int:
	num_str = ''
	roman_list = list(roman_str)
	i = 0
	token_start = -1
	try:
		while(i < len(roman_list)):
			if roman_list[i] in OPERATOR_LIST:
				if token_start > -1:
					roman_numeral = roman_list[token_start:i]
					num_str += str(convert_roman_numeral_to_number(roman_numeral))
					token_start = -1
				num_str += roman_list[i]
				i += 1
			elif token_start > -1:
				i += 1
			else:
				token_start = i
				i += 1
		if token_start > -1:
			roman_numeral = roman_list[token_start:i]
			num_str += str(convert_roman_numeral_to_number(roman_numeral))
		num_str = num_str.replace('^', '**')
		return eval(num_str)
	except Exception as e:
		raise ValueError("Unable to calculate value")
