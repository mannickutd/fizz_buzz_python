import math


def is_perfect_square(x:int) -> bool:
    '''
    https://www.geeksforgeeks.org/check-number-fibonacci-number/
    ''' 
    s = int(math.sqrt(x)) 
    return s*s == x


def is_fibonacci(n:int) -> bool:
    '''
    https://www.geeksforgeeks.org/check-number-fibonacci-number/
    '''
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)


def is_fizz_buzz_number(num:int) -> str:
    '''
        Return a str representation of the number.
        for multiples of three return “Fizz” instead of the
        number and for multiples of five return “Buzz”.
        For numbers which are multiples of both three and five return
        “FizzBuzz”. Return “Flamingo” when a number is a member of
        the Fibonacci sequence, and “Pink Flamingo” when it is a
        multiple of 3 and 5 and a member of the Fibonacci sequence.
    '''
    if num <= 0:
        return str(num)
    div_by_three = num % 3
    div_by_five = num % 5
    fib_num = is_fibonacci(num)
    if div_by_three == 0 and div_by_five == 0:
        if fib_num:
            return 'Pink Flamingo'
        return 'FizzBuzz'
    elif div_by_three == 0:
        return 'Fizz'
    elif div_by_five == 0:
        return 'Buzz'
    elif fib_num:
        return 'Flamingo'
    else:
        return str(num)
