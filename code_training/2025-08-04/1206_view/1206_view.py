"""
1.아이디어
조망권획득하려면 인덱스를 양쪽으로 왼2 왼1 오1 오2 값들을 본인빌딩이랑 계산.
그 값중에서 최솟값이 조망권 획득한 세대수임
"""

import sys
sys.stdin = open("input.txt")

# 테스트케이스 고정
T = 10

for t in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))

    # 조망권획득한 가구 수 더해줄 변수 생성
    cnt = 0
    # 왼쪽오른쪽 끝 2개는 0이므로 범위 2 ~ N-2 설정
    for i in range(2, N - 2):
        # 왼2,1 오른1,2 각각 조망권있는지 계산
        left2 = buildings[i] - buildings[i - 2]
        left1 = buildings[i] - buildings[i - 1]
        right1 = buildings[i] - buildings[i + 1]
        right2 = buildings[i] - buildings[i + 2]
        # 각 계산값에서 최솟값구해주고
        min_value = min(left2, left1, right1, right2)
        # 음수일 경우 0을 더해준다
        cnt += max(0, min_value)
    print(f"#{t} {cnt}")