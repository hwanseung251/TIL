import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 꽃가루 수가 가장 많은 경우의 변수를 저장하는 변수
    max_value = 0

    for i in range(N):
        for j in range(M):
            # 총 터지는 풍선의 꽃가루 수를 카운트해주는 변수
            cnt = 0
            # 현재 지정한 풍선의 꽃가루 수
            pollen = arr[i][j]
            # 일단 현재 꽃가루를 더해줌
            cnt += pollen

            di = [0, 1, 0, -1]
            dj = [1, 0, -1, 0]

            for d in range(4):
                # 현재 꽃가루 수만큼 주변 풍선이 터지므로 이를 고려해준다
                for k in range(1, 1+pollen):
                    ni = i + di[d]*k
                    nj = j + dj[d]*k

                    if 0<=ni<N and 0<=nj<M:
                        cnt += arr[ni][nj]

            max_value = max(max_value, cnt)

    print(f"#{t} {max_value}")

