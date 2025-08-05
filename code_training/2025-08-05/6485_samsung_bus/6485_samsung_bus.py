import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    # A 정류장과 B 정류장을 저장할 리스트를 생성한다
    # 정류장 번호는 1부터 5000까지 이므로 인덱스 0은 사용하지 않는다
    A_lst = [0] * (N+1)
    B_lst = [0] * (N+1)
    # 각 노선마다 A정류장과 B정류장을 입력받고 생성해둔 리스트에 저장한다
    for i in range(1, N+1):
        A, B = map(int, input().split())
        A_lst[i] = A
        B_lst[i] = B

    P = int(input())
    result = []
    # P개의 버스 정류장을 돌면서
    for _ in range(1, P+1):
        C = int(input())
        # 주어진 정류장에 버스 노선이 지나는 수를 카운팅해주는 변수 생성
        cnt = 0

        # 번호가 A이상이고 B이하인 개수를 센다
        for i in range(1, N+1):
            if A_lst[i] <= C <= B_lst[i]:
                cnt += 1

        result.append(cnt)

    print(f"#{t} {' '.join(map(str, result))}")