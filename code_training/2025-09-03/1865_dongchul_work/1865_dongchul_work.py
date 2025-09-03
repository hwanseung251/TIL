import sys
sys.stdin = open("input.txt")


def chk_percent(worker, included, current_per):
    global max_per
    if worker == N:
        max_per = max(max_per, current_per)
        return

    for i in range(N):
        if included[i]:
            continue
        n_per = current_per * success_percent[worker][i] * 0.01
        if n_per <= max_per:
            continue
        included[i] = True
        chk_percent(worker+1, included, n_per)
        included[i] = False

T = int(input())

for t in range(1, T+1):
    N = int(input())

    success_percent = [list(map(int, input().split())) for _ in range(N)]

    max_per = 0
    chk_percent(0, [False]*N, 1)

    print(f"#{t} {max_per*100:.6f}")
