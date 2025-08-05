import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    power = list(map(int, input().split()))

    #전기버스의 현재 위치, 충전 수를 저장할 변수를 생성한다
    current_point = 0
    cnt = 0
    # 다음 충전이 불가능할때를 체크해줄 bool변수를 생성한다
    chk = False

    # 현재 위치에서 최대 이동거리 K를 더해줘도 종점을 넘지 못한다면 무한 반복한다
    while current_point+K < N:
        # 최대거리부터 순차적으로 충전기의 위치를 체크해주고 충전기가 있으면 이동한다
        for i in range(current_point+K, current_point, -1):
            if i in power:
                current_point = i
                cnt += 1
                break
        else:
            # 만약 충전기로 이동할 수 없다면 체크해준다
            chk = True
            break

    # 체크가 되어있다면 0을
    if chk == True:
        print(f"#{t} {0}")
    # 그렇지 않다면 cnt를 출력
    else:
        print(f"#{t} {cnt}")