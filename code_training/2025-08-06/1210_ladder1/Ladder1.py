import sys
sys.stdin = open("input.txt")

T = 10

for t in range(1, T+1):
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    # 양옆에 길이 있는지 확인하기 위한 델타 탐색
    di = [0, 0]
    dj = [1, -1]
    # 첫번째 행을 돌며 출발지점을 찾는다
    for start in range(100):
        # 만약 출발지점이 정해지면
        if arr[0][start] == 1:
            # 그지점의 좌표를 저장하고
            i, j = 0, start
            # 배열이 지난곳인지 안지난곳인지 체크할 체크 배열 생성
            chk = [[False] * 100 for _ in range(100)]

            # (i가 99면 맨마지막까지 내려온것) 다 내려오기 한칸 전까지 반복
            while i < 99:
                # 아직 가지않은곳이면
                chk[i][j] = True
                # 왼쪽
                # j가 0보다 커야 왼쪽으로 갈 수 있음 / 왼쪽 칸이 1인지 체크 / 이미 지나온 곳이 아닌지 체크
                if j > 0 and arr[i][j - 1] == 1 and not chk[i][j - 1]:

                    # 왼쪽이 계속 1이면 계속 왼쪽으로 이동
                    while j > 0 and arr[i][j - 1] == 1:
                        j -= 1
                        chk[i][j] = True
                # 오른쪽
                # j가 99보다 작아야 오른쪽으로 갈 수 있음 / 오른쪽 칸이 1인지 체크 / 오른쪽 칸이 이미 지난곳이 아닌지 체크
                elif j < 99 and arr[i][j + 1] == 1 and not chk[i][j + 1]:

                    # 오른쪽이 계속 1이면 계속 오른쪽으로 이동
                    while j < 99 and arr[i][j + 1] == 1:
                        j += 1
                        chk[i][j] = True
                # 그렇지 않으면 계속 아래로 간다
                i += 1

            # while문을 나왔을땐 마지막 행에 도착을 한거임
            # 도착했을 때 2이면 출발지점 반환
            if arr[i][j] == 2:
                print(f"#{tc} {start}")
                break




