import sys
sys.stdin = open("input.txt")
# 재귀를 이용한 풀이
T = int(input())

def recur(N):
    if N == 1:
        return [1]

    next_list = [0] * N
    now_list = [0] + recur(N-1) + [0]

    for i in range(N):
        next_list[i] = now_list[i] + now_list[i+1]

    return next_list

for t in range(1, T+1):
    n = int(input())
    print(f"#{t}")
    for i in range(1, n+1):
        print(*recur(i))