# DFS
### 개념
'''
- 그래프 탐색 종류
    - DFS : Depth-first search(깊이 우선 탐색)
    - 스택 과 재귀 로 해결가능
    - 스택 활용은 BFS 랑 유사함
    - 따라서 재귀로 해결해보겠음
- 재귀함수
    - 자기 자신을 다시 호출하는 함수
    - 주의할점 
        - 재귀 함수가 종료되는 시점 반드시 명시
        - 재귀함수의 깊이가 너무 깊어지면 Stack Overflow
    - DFS, 백트래킹에서 주로 사용

- 아이디어
    - 시작점에 연결된 Vertex 찾기
    - 연결된 Vertex를 계속해서 찾음(끝날 때 까지)
    - 더이상 연결된 Vertex 없을경우 다음

- 시간복잡도: 
    - DFS : O(V + E) 

- 자료구조
    - 검색할 그래프: 2차원 배열
    - 방문여부 확인: 2차원 배열(재방문 금지)
'''
## 백준 2667
import sys
input = sys.stdin.readline
N = int(input())
Map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []
each_size = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def dfs(y, x):
    global each_size
    each_size += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if Map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny ,nx)


for j in range(N):
    for i in range(N):
        if Map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] =True
            each_size = 0
            dfs(j, i)
            result.append(each_size)
result.sort()
print(len(result))
for i in result:
    print(i)
