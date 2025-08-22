import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    used = [False] * N
    best = float("inf")

    def DFS(r, s):
        global best
        if s >= best:
            return
        if r == N:
            best = s
            return
        for i in range(N):
            if not used[i]:
                used[i] = True
                DFS(r+1, s + numbers[r][i])
                used[i] = False

    DFS(0,0)
    print(f"#{t} {best}")