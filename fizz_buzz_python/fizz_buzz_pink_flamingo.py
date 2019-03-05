

def is_fizz_buzz_number(num:int) -> str:
    '''
        Return a str representation of the number.
        for multiples of three return “Fizz” instead of the
        number and for multiples of five return “Buzz”.
        For numbers which are multiples of both three and five return “FizzBuzz”
    '''
    if num <= 0:
        return str(num)
    div_by_three = num % 3
    div_by_five = num % 5
    if div_by_three == 0 and div_by_five == 0:
        return 'FizzBuzz'
    if div_by_three == 0:
        return 'Fizz'
    elif div_by_five == 0:
        return 'Buzz'
    else:
        return str(num)
