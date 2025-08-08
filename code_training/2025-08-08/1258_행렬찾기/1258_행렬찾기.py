import sys
sys.stdin = open("input.txt")

T = int(input())

def find_weapon(i, j):
    row, col = 0, 0

    # i에서 현재 행만큼 갔을 때 벽체크
    # 웨어하우스에 0이 아닌지 체크
    # 아니면 행만큼 계속 가준다
    while i + row < n and ware_house[i + row][j] != 0:
        row += 1

    # j에서 현재 열만큼 갔을 때 벽체크
    # 웨어하우스에 0이 아닌지 체크
    # 아니면 열만큼 계속 가준다
    while j + col < n and ware_house[i][j + col] != 0:
        col += 1

    # 방문 체크
    for x in range(i, i + row):
        for y in range(j, j + col):
            chk[x][y] = True

    return row, col, row * col


for t in range(1, T+1):
    n = int(input())
    ware_house = [list(map(int, input().split())) for _ in range(n)]
    chk = [[False]* n for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if ware_house[i][j] != 0 and chk[i][j] == False:
                result.append(find_weapon(i,j))

    result.sort(key = lambda x : (x[2], x[0]))
    print(f"#{t} {len(result)}", end = " ")
    for r, c, rc in result:
        print(r, c, end = " ")