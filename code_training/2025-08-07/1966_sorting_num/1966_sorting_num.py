import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 선택정렬
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]

    print(f"#{t} {' '.join(map(str, numbers))}")