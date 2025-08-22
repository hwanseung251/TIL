import sys
sys.stdin = open("input.txt")

import itertools

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_value = float("inf")
    
    # 순열로하면 런타임 에러!! 조합으로 해야함
    for A in itertools.combinations(range(N), N//2):
        B = [i for i in range(N) if i not in A]

        A_taste = 0
        for a,b in itertools.combinations(A, 2):
            A_taste += arr[a][b]+arr[b][a]

        B_taste = 0
        for a, b in itertools.combinations(B, 2):
            B_taste += arr[a][b] + arr[b][a]
            # B_taste를 키워가며 빼는데 벌써부터 작으면
        min_value = min(min_value, abs(A_taste - B_taste))


    print(f"#{t} {min_value}")