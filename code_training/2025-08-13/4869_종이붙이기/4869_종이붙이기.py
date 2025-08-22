import sys
sys.stdin = open("input.txt")

T = int(input())


def recur(num):
    if num == 1:
        return 1
    elif num == 2:
        return 3

    return recur(num-2)*2 + recur(num-1)


for t in range(1, T+1):
    N = int(input())
    print(f"#{t} {recur(N // 10)}")
