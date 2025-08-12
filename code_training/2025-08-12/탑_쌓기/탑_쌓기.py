import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, W1, W2 = map(int, input().split())

    k = list(map(int, input().split()))

    # 무게가 가벼우면 젤 위층에 놔야함. 오름차순 정렬해주기
    k.sort()

    # 최소비용 입력변수 생성
    min_cost = 0
    for i in k:
        # W1이 W2보다 높거나 같으면 맨 위층에 젤 가벼운 물건 놓기
        if W1 >= W2:
            min_cost += i*W1
            # 이미 놓은 곳은 제외
            W1 -= 1
        # W2가 더 높으면 여기에 놓기
        else:
            min_cost += i*W2
            W2 -= 1
    print(f"#{t} {min_cost}")