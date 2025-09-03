import sys
sys.stdin = open("input.txt")
from itertools import combinations

def chk_subset(i, j):
    """ (i,j)에서 시작하는 M개의 꿀 중, 용량 C 이하로 고른 부분집합의 '제곱합' 최댓값 """
    arr = [honey[i][j+m] for m in range(M)]
    n = len(arr)
    best = 0

    # 모든 부분집합 순회
    for mask in range(1 << n):
        sum_val = 0   # 선택한 꿀의 합 (용량 체크용)
        sum_sq  = 0   # 선택한 꿀의 제곱합 (평가 점수)
        valid = True
        for k in range(n):
            if mask & (1 << k):
                sum_val += arr[k]
                if sum_val > C:   # 용량 초과 시 이 부분집합은 패스
                    valid = False
                    break
                sum_sq += arr[k] * arr[k]
        if valid:
            best = max(best, sum_sq)

    # 가장 최대의 원소 제곱합이 반환됨
    return best


T = int(input())

for t in range(1, T+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    # 최대의 수익을 저장할 변수
    max_cost = 0
    # 가능한 시작점을 모두 subsets에 넣음
    subsets = []
    for i in range(N):
        for j in range(N-M+1):
            subsets.append((i, j))

    # 시작점에서 두개를 고르는데 겹치지 않는 두 시작점을 골라줌
    for a, b in combinations(subsets, 2):
        if a[0] == b[0]:
            if a[1] < b[1]:
                if a[1] + M - 1 >= b[1]:
                    continue
            if a[1] > b[1]:
                if b[1] + M - 1 >= a[1]:
                    continue

        # 수익 갱신
        current_cost = chk_subset(a[0], a[1]) + chk_subset(b[0], b[1])
        max_cost = max(max_cost, current_cost)

    print(f"#{t} {max_cost}")