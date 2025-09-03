import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    set_A = [i for i in range(1,13)]
    cnt = 0
    N, K = map(int, input().split())

    for i in range(1<<12):
        subset = []
        for j in range(12):
            if i & (1<<j):
                subset.append(set_A[j])
            if sum(subset) > K:
                break
            if len(subset) > N:
                break
        if len(subset) == N and sum(subset) == K:
            cnt += 1

    print(f"#{t} {cnt}")