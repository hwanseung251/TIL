import sys
sys.stdin = open("input.txt")

def find_longest(value, i, j, chance=True, visited = None):
    if visited is None:
        visited = set()
    # 재귀 호출하면서 가장 최대로 긴 등산로인 경우의 값을 넣어주는 변수
    current_long = 1
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        # 범위에 안벗어나고 방문하지 않은 곳이면
        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
            # 다음 높이를 nh변수에 저장
            nh = my_map[ni][nj]
            # 다음 높이와 현재 높이를 비교, 다음 높이가 작으면 방문여부 넣어주고 current_long 갱신
            if value > nh:
                visited.add((ni,nj))
                current_long = max(current_long, 1 + find_longest(nh, ni, nj, chance, visited))
                # 방문을 체크하고 재귀호출을 했으면 다시 다음을 위해 방문을 해제해줌
                visited.remove((ni, nj))
            # 다음칸에서 높이를 K만큼 깎았을때 갈 수 있는 경우이고 아직 한번도 기회를 쓰지 않았을 경우
            elif (value > (nh - K)) and chance:
                visited.add((ni, nj))
                current_long = max(current_long, 1 + find_longest(value-1, ni, nj, False, visited))
                visited.remove((ni, nj))
    return current_long

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    my_map = [list(map(int, input().split())) for _ in range(N)]

    # 출발지점은 항상 가장 높은 봉우리에서만 가능하므로
    # 최대 봉우리 값 계산
    highest = 0
    for lst in my_map:
        high = max(lst)
        highest = max(highest, high)

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 최대 봉우리가 여러개이면 각 봉우리에서 가장 긴 등산로값을 저장
    max_value = 0
    for i in range(N):
        for j in range(N):
            if my_map[i][j] == highest:
                max_value = max(find_longest(my_map[i][j], i, j, True, {(i,j)}), max_value)

    print(f"#{t} {max_value}")
