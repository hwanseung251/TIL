T = int(input())

for t in range(1, T+1):
    matrix = [[False]*10 for _ in range(10)]
    N = int(input())

    # 파란색을 담아줄 리스트 생성
    blue_list = []
    for _ in range(N):
        #색칠할영역을 입력받고
        square = list(map(int, input().split()))
        # 빨간색이면 True를 표시한다
        if square[-1] == 1:
            for i in range(square[1], square[3]+1):
                for j in range(square[0], square[2]+1):
                    matrix[i][j] = True
        # 파란색이면 일단 파란색 리스트에 담아둔다
        elif square[-1] == 2:
            blue_list.append(square)

    # 모든 색이 칠해지는 칸을 카운팅하는 변수
    cnt = 0
    # 담아둔 파란색 리스트를 하나씩 꺼내와서 만약 빨간색이 색칠되어있을경우 카운트를해준다
    for blue in blue_list:
        for i in range(blue[1], blue[3]+1):
            for j in range(blue[0], blue[2]+1): #열(row)index들로 range돌림. 즉 y축
                if matrix[i][j] == True:
                    cnt += 1

    print(f"#{t} {cnt}")