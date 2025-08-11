import sys
sys.stdin = open("input.txt")

T = int(input())

my_str = ['b', 'd', 'p', 'q']
my_str_reverse = ['d', 'b', 'q', 'p']

for t in range(1, T+1):
    input_str = list(input())
    result = ''
    for s in input_str:
        for i in range(4):
            if s == my_str[i]:
                result += my_str_reverse[i]
    result = result[::-1]
    print(f"#{t} {result}")