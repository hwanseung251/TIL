import sys
sys.stdin = open("input.txt")

T = 10

for t in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0

    for i in range(2, N-2):
        left2 = buildings[i] - buildings[i-2]
        left1 = buildings[i] - buildings[i-1]
        right1 = buildings[i] - buildings[i+1]
        right2 = buildings[i] - buildings[i+2]
        my_lst = []
        my_lst.extend([left2, left1, right1, right2])
        min_value = my_lst[0]

        for val in my_lst[1:]:
            if min_value > val:
                min_value = val
        if min_value > 0:
            cnt += min_value
        # min_value = min(left2, left1, right1, right2)
        # cnt += max(0, min_value)
    print(f"#{t} {cnt}")