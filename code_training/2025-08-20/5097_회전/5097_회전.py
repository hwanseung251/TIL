import sys
sys.stdin = open("input.txt")

from collections import deque
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    queue.rotate(-M)

    print(f"#{t} {queue.popleft()}")