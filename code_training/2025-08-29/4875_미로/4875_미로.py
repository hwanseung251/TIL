import sys
sys.stdin = open("input.txt")

def dfs(i, j):
    global find
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < N and 0 <= nj < N:
            if miro[ni][nj] == 0 and chk[ni][nj] == False:
                chk[ni][nj] = True
                dfs(ni, nj)
            # 도착지점을 발견했을 때 find변수를 True로 변환
            elif miro[ni][nj] == 3:
                find = True
    return find


T = int(input())

for t in range(1, T+1):
    N = int(input())
    miro = [list(map(int, list(input()))) for _ in range(N)]
    chk = [[False] * N for _ in range(N)]
    # 미로를 찾았는지 못찾았는지 나타내는 변수
    find = False

    for i in range(N):
        for j in range(N):
            # 출발지점을 발견하면 dfs탐색
            if miro[i][j] == 2:
                if dfs(i, j):
                    print(f"#{t} 1")
                else:
                    print(f"#{t} 0")
