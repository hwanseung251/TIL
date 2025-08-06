def get_final_position(commands):
    # 시작 위치
    r, c = 0, 0

    # 델타 배열 정의 (N, S, E, W 순서)
    # 각 방향에 대한 행(r), 열(c)의 변화량
    dr = [-1, 1, 0, 0]  # 행(row) 변화량
    dc = [0, 0, 1, -1]  # 열(column) 변화량

    # 명령어와 델타 인덱스를 매핑
    directions = ['N', 'S', 'E', 'W']

    # 주어진 명령어(commands)를 하나씩 순회
    for cmd in commands:
        # directions 리스트에서 현재 명령어(cmd)의 인덱스를 찾음
        for i in range(len(directions)):
            if cmd == directions[i]:
                # 해당 인덱스의 dr, dc 값을 현재 위치에 더함
                r += dr[i]
                c += dc[i]
                break  # 해당 명령어를 처리했으면 다음 명령어로 넘어감

    return r, c
commands = ['E', 'E', 'S', 'W', 'N']
end_r, end_c = get_final_position(commands)
print(f"최종 위치: ({end_r}, {end_c})") # 최종 위치: (0, 1)