import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    min_idx = 0
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if ai[min_idx] > ai[j]:
                min_idx = j
        ai[min_idx], ai[i] = ai[i], ai[min_idx]

    result = []
    i = 1
    for _ in range(5):
        result.append(ai[-i])
        result.append(ai[i-1])
        i += 1
    print(f"#{t} {' '.join(map(str, result))}")