import sys
sys.stdin = open("input.txt")

T = 10

def max_pal_len(arr):
    # 행/열을 미리 문자열로 만들어둠
    rows = [''.join(r) for r in arr]
    # 전치를 활용
    cols = [''.join(c) for c in zip(*arr)]

    # 큰 길이부터 검사
    for N in range(100, 0, -1):
        # 행 검사: 하나라도 나오면 바로 그 N 리턴
        for i in range(101 - N):
            for s in rows:
                if s[i:i+N] == s[i:i+N][::-1]:
                    return N
        # 열 검사
        for j in range(101 - N):
            for s in cols:
                if s[j:j+N] == s[j:j+N][::-1]:
                    return N
    return 0

for _ in range(T):
    tc = int(input().strip())
    arr = [list(input().strip()) for _ in range(100)]
    print(f"#{tc} {max_pal_len(arr)}")
