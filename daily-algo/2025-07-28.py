import sys
input = sys.stdin.readline

N = int(input())
pipe = [[0] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    pipe[i] = [0] + list(map(int, input().split()))
print(pipe)