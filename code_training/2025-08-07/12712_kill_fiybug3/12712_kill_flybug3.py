import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
	#8방향 델타
    di = [0, 1, 0, -1, 1, 1, -1, -1]
    dj = [1, 0, -1, 0, 1, -1, 1, -1]

    max_value = 0
    for i in range(N):
        for j in range(N):

            cnt = arr[i][j]
		    #상하좌우
            for d in range(0, 4):
		        # 가운데 중복더함 방지를 위해 1부터
                for m in range(1,M):
                    ni = i + di[d] * m
                    nj = j + dj[d] * m

                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            max_value = max(max_value, cnt)

            cnt = arr[i][j]
			#대각선방향
            for d in range(4, 8):
		        # 가운데 중복더함 방지를 위해 1부터
                for m in range(1,M):
                    ni = i + di[d] * m
                    nj = j + dj[d] * m

                    if 0 <= ni < N and 0 <= nj < N:
                        cnt += arr[ni][nj]
            max_value = max(max_value, cnt)


    print(f"#{t} {max_value}")