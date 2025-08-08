import sys
sys.stdin = open("input.txt")

T = int(input())

def itoa(integer_value):
    if integer_value == 0:
        return '0'

    is_negative = integer_value < 0
    if is_negative:
        integer_value = -integer_value

    result = ''
    while integer_value > 0:
        remainder = integer_value % 10
        result = chr(48 + remainder) + result
        integer_value //= 10

    if is_negative:
        result = "-" + result

    return result


for t in range(1, T+1):
    number = int(input())
    result = itoa(number)
    print(f'#{t} {result}', type(result))