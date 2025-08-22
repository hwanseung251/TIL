import sys
sys.stdin = open("input.txt")

T = int(input())


def max_percent(n, per=1):
    global max_per

    if per <= max_per:
        return

    if n == N:
        max_per = max(max_per, per)

    for i in range(N):
        if chk[i]:
            continue
        chk[i] = True
        max_percent(n+1, per*arr[n][i]*0.01)
        chk[i] = False


for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(float, input().split())) for _ in range(N)]
    chk = [False] * N

    max_per = 0
    max_percent(0, 1)

    print(f"#{t} {max_per*100:.6f}")








