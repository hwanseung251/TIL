import sys
sys.stdin = open("input.txt")

"""
즉 원소들의 합이 B 이상이면서 최소인 값을 구하는 것
"""

def make_top(depth, current):
    global min_value
    if current >= min_value:
        return
    if current >= B:
        min_value = min(min_value, current)
        return
    if depth == N:
        return

    make_top(depth+1, current)
    make_top(depth+1, current+clerk[depth])

T = int(input())

for t in range(1, T+1):
    N, B = map(int, input().split())
    clerk = list(map(int, input().split()))

    min_value = float("inf")
    make_top(0, 0)

    print(f"#{t} {min_value - B}")