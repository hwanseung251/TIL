"""
시작점
back = (1,1)
front = (1,2)

front - back = (0,1) 가로로 되어있음
- back = front
  front = (, +1) or (+1, +1)

front - back = (1,0) 세로로 되어있음
  front = (+1, ) or (+1, +1)


front - back = (1,1) 대각선으로 되어있음
  front = (, +1) or (+1, +1) or (+1, )

"""

import sys
input = sys.stdin.readline

N = int(input())
pipe_map = [[0] * (N+1) for _ in range(N+1)]
cnt = 0

for i in range(1,N+1):
    pipe_map[i] = [0] + list(map(int, input().split()))


def recur(back, front):
    global cnt
    if front == [N,N]:
        cnt += 1
        return cnt

    if chk_direction(back, front) == '가로':
        # 다음 갈부분이 0이면 전진!
        if (pipe_map[front[0]+1][front[1]] == 0) and (front[0]+1 < N):
            back = front
            front = [front[0]+1, front[1]]
            return recur(back, front)
        elif (pipe_map[front[0]+1][front[1]+1] == 0) and (front[0]+1 < N) and (front[1]+1 < N):
            back = front
            front = [front[0]+1, front[1]+1]
            return recur(back, front)
        else:
            return cnt
        
    elif chk_direction(back, front) == '세로':
        if (pipe_map[front[0]][front[1]+1] == 0) and (front[1]+1 < N):
            back = front
            front = [front[0], front[1]+1]
            return recur(back, front)
        elif (pipe_map[front[0]+1][front[1]+1] == 0) and (front[0]+1 < N) and (front[1]+1 < N):
            back = front
            front = [front[0]+1, front[1]+1]
            return recur(back, front)
        else:
            return cnt
    elif chk_direction(back, front) == '대각선':
        if (pipe_map[front[0]+1][front[1]] == 0) and (front[0]+1 < N):
            back = front
            front = [front[0]+1, front[1]]
            return recur(back, front)
        elif (pipe_map[front[0]+1][front[1]+1] == 0) and (front[0]+1 < N) and (front[1]+1 < N):
            back = front
            front = [front[0]+1, front[1]+1]
            return recur(back, front)
        elif (pipe_map[front[0]][front[1]+1] == 0) and (front[1]+1 < N):
            back = front
            front = [front[0], front[1]+1]
            return recur(back, front)
        else:
            return cnt
        
def chk_direction(back, front):
    if (front[0] - back[0]) == 1 and (front[1] - back[1]) == 0:
        return '가로'
    elif (front[0] - back[0]) == 0 and (front[1] - back[1]) == 1:
        return '세로'
    else:
        return '대각선'
back = [1,1]
front = [2,1]

for j in range(1,N+1):
    for i in range(1, N+1):
        if [j, i] == front:
            result = recur(back, front)
print(result)