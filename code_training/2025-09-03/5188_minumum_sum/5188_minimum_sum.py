import sys
sys.stdin = open("input.txt")

def dfs(i,j, result):
    global min_value
    if i == N-1 and j == N-1:
        min_value = min(min_value, sum(result))
        return min_value
    # 오른쪽과 아래만 감
    di = [0, 1]
    dj = [1, 0]
    for d in range(2):
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<N and 0<=nj<N:
            # 현재 최소보다 크면 continue(break하면 다른방향까지 종료해버리게 되서 continue해야함)
            if (sum(result) + arr[ni][nj]) >= min_value:
                continue
            dfs(ni,nj, result + [arr[ni][nj]])


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_value = float("inf")
    dfs(0,0,[arr[0][0]])
    print(f"#{t} {min_value}")