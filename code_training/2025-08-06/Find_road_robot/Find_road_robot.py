def get_final_position(commands):
    # 시작 위치
    r, c = 0, 0
    arr = [[0]*5 for _ in range(5)]

    for direction in commands:
        if direction == 'N':
            if 0 <= r-1 < 5:
                r -= 1
        elif direction == 'S':
            if 0 <= r+1 < 5:
                r += 1
        elif direction == 'E':
            if 0 <= c+1 < 5:
                c += 1
        elif direction == 'W':
            if 0 <= c-1 < 5:
                c -= 1
    return r, c

commands = ['E', 'E', 'S', 'W', 'N']
end_r, end_c = get_final_position(commands)
print(f"최종 위치: ({end_r}, {end_c})")
