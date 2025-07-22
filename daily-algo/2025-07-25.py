# BFS
### 개념
"""
- 그래프 탐색: 어떤 것들이 연속해서 이어질 떄, 모두 확인하는 방(Vertex + Edge)
- 그래프 탐색 종류
    - BFS : 너비 우선 탐색
    - DFS : 깊이 우선 탐색

### 아이디어
- 시작점에 연결된 Vertex 찾기
- 찾은 Vertex를 Queue에 저장
- Queue의 가장 먼저 들어간 Vertex를 뽑아서 반복

### 시간복잡도
- O(V + E)
    - V: Vertex의 개수
    - E: Edge의 개수

### 자료구조
- 검색할 그래프
- 방문여부 확인
- Queue(BFS 실행)
"""
## 백준 1926
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edge = [list(map(int, input().split())) for _ in rannge(n)]
chk = [[False]*m for _ in range(n)]
cnt = 0
max_value = 0
queue = deque()

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs(y, x):
    rs = 1
    queue.append([y, x])
    while queue:
        ey, ex = queue.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if edge[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    queue.append([ny, nx])
    return rs

for j in range(n):
    for i in range(m):
        if edge[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            max_value = max(max_value, bfs([j,i]))
            cnt += 1
print(cnt)
print(max_value)