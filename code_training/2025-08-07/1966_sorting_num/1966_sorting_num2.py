import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 버블 정렬
    for i in range(N-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print(f"#{t} {' '.join(map(str, numbers))}")