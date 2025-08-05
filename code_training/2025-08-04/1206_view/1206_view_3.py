import sys
sys.stdin = open("input.txt")

T = 10  # testcase 10개 주어짐

for t in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))

    cnt = 0

    for i in range(2, N-2):
        for j in range(buildings[i], 0, -1):
            if j > buildings[i-2] and j > buildings[i-1] and j > buildings[i+1] and j > buildings[i+2]:
                cnt += 1
            else:
                break
    print(f"#{t} {cnt}")