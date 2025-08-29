import sys
sys.stdin = open("input.txt")

T = int(input())

def dfs(start):
    global chk
    stack = [start]

    while stack:
        current = stack.pop()

        for next_node in village[current]:
            if not chk[next_node]:
                chk[next_node] = True
                stack.append(next_node)
    return 1


for t in range(1, T+1):
    N, M = map(int, input().split())
    village = [[] for _ in range(N+1)]
    chk = [False] * (N+1)
    cnt = 0

    for _ in range(M):
        n1, n2 = map(int, input().split())
        village[n1].append(n2)
        village[n2].append(n1)

    for n in range(1, N+1):
        if village[n] and chk[n] == False:
            cnt += dfs(n)

    # 혼자만 존재하는 그룹 카운팅
    for i in range(1, N+1):
        if not village[i]:
            cnt += 1

    print(f"#{t} {cnt}")
