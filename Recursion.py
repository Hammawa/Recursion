#Abdullah Hammawa, 1619949
def mylen(some_list):
    '''Determines the length of a list recursively'''
    empty_list = []
    if some_list == empty_list:
        length = 0
        return length
    else:
        some_list.pop()
        length = mylen(some_list) + 1
    return length


def intDivision(dividend, divisor):
    '''Takes a dividen and divisor and preforms integer division'''
    try:
        dividend = int(dividend)
        divisor = int(divisor)
    except:
        print("The value you enter must be an integer")
    valid_input = (isinstance(dividend, int) and isinstance(divisor, int) and dividend >= 0 and divisor > 0)
    assert valid_input == True, "The dividend and divisor must both be positive integers"
    if dividend < divisor:
        integer_result = 0
        return integer_result
    elif dividend == divisor:
        integer_result = 1
        return integer_result
    else:
        #for every time we can still fit the divisor into the dividend we add one 
        dividend -= divisor
        integer_result = intDivision(dividend, divisor) + 1
        return integer_result

def main():
    n = input('Enter an integer dividend: ')
    m = input('Enter an integer divisor: ')
    print('Integer division', n, '//', m, '=', intDivision(n,m))
main()

def sumdigits(number):
    '''Takes a number and returns the sum of its digits'''
    try:
        number = int(number)
    except:
        print("The value you enter must be an integer")    
    is_integer = (isinstance(number, int) and number > 0)
    assert is_integer == True, "The number you input must be a positive integer"
    number_string = str(number)
    if len(number_string) == 1:
        return number_string
    else:
        #have to add the last number from the string of digits before you remove that digit
        i = len(number_string) - 1
        add_on = number_string[i]
        number_string = number_string[:-1]
        number = int(number_string)
        result = int(sumdigits(number)) + int(add_on)
    return result


def reverseDisplay(digits):
    '''This function takes a number and then returns another number made up of the digits of the original number in reverse order, e.g. 123 to 321'''
    try:
        digits = int(digits)
    except:
        print("The value you enter must be an integer")
    is_integer = (isinstance(digits, int) and digits > 0)
    assert is_integer == True, "The number you input must be a positive integer"
    digit_str = str(digits)
    if len(digit_str) == 1:
        return digit_str
    else:
        #takes the last digit and adds it onto the front of this new string
        i = len(digit_str) - 1 
        digit_to_insert = digit_str[i]
        digit_str = digit_str[:-1]
        result = digit_to_insert + reverseDisplay(int(digit_str)) 
    return result


def binary_search2(key,alist,lowerBound,upperBound):
    '''Takes a key, list, lower bound and upper bound as inputs and returns the index of the given key. Returns negative 1 if said key does not exist in the list '''
    found = False
    guessIndex = (upperBound+lowerBound)//2
    if (key == alist[guessIndex]): 
        return guessIndex
    #condition when the binary search has done the whole list
    elif upperBound == lowerBound:
        guessIndex = -1
    else:
        if (key > alist[guessIndex]):
            upperBound = guessIndex - 1
        else:
            lowerBound = guessIndex + 1  
        guessIndex = binary_search2(key,alist,lowerBound,upperBound)
    return guessIndex


