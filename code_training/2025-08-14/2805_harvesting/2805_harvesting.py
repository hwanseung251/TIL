import sys
sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input().strip())) for _ in range(N)]

    mid = N // 2
    result = 0
    for i in range(N):
        # 중간값에서 절댓값을 활용해 커졌다 작아지는 cut_num 생성
        cut_num = abs(mid - i)
        # cut_num을 기점으로 슬라이싱한 값만 result에 더해준다.
        result += sum(farm[i][cut_num:N - cut_num])

    print(f"#{t} {result}")