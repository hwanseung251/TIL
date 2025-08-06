import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 양옆에 길이 있는지 확인하기 위한 델타 탐색
    di = [0, 0]
    dj = [1, -1]

    for start in range(100):

        if arr[0][start] == 1:
            chk = [[False] * 100 for _ in range(100)]
            i, j = 0, start

            while i<99:
                chk[i][j] = True

                for d in range(2):
                    ni = i + di[d]
                    nj = j + dj[d]

                    if 0<=ni<100 and 0<=nj<100 and arr[ni][nj] == 1 and chk[ni][nj] == False:
                        i, j = ni, nj
                        chk[i][j] = True
                        break
                else:
                    ni = i + 1
                    if 0<=ni<100:
                        i = ni
                        chk[i][j] = True

        if arr[i][j] == 2:
            print(f"#{tc} {start}")
            break