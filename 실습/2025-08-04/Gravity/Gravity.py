import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    box_room = list(map(int, input().split()))

    # 최대로 낙하한 값을 0으로 초기설정
    max_value = 0

    # 맨 왼쪽 박스들부터 낙하값 체크
    for i in range(N):
        # 본인보다 작은 값을 저장할 변수 생성
        cnt = 0
        # 포문을 돌면서 본인보다 작은 애들이 있을때마다
        # cnt += 1
        for j in range(i + 1, N):
            if box_room[i] > box_room[j]:
                cnt += 1
        # cnt값이 현재 max_value보다 크면 갱신
        if max_value < cnt:
            max_value = cnt
    print(f"#{i} {max_value}")