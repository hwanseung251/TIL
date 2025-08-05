"""
왼쪽부터 박스를 포문돌면서 최고길이 박스와 최저 길이 박스 선택해주는 코드 필요
최고 길이 박스에서 최저길이 박스로 1 덤프
덤프 제한 횟수만큼 위 반복
다돌면 최고 최저 높이차 반환

만약 횟수가 다 안끝났는데 덤프수행이 완료되었으면 (최고 - 최저 가 0 또는 1)
높이 차를 반환
"""
import sys
sys.stdin = open("input.txt")

T = 10
for t in range(1, T+1):
    dump_num = int(input())
    box_heights = list(map(int, input().split()))

    # 덤프 가능 횟수만큼 포문을 돈다
    for _ in range(dump_num):

        # 최대 최소 값과 인덱스를 각각 저장할 변수를 생성한다
        max_value, max_index = box_heights[0], 0
        min_value, min_index = box_heights[0], 0

        # 박스 높이 리스트 만큼 포문을 돌면서 최소, 최대 값과 인덱스를 갱신해준다
        for i in range(len(box_heights)):
            if box_heights[i] > max_value:
                max_value, max_index = box_heights[i], i
            elif box_heights[i] < min_value:
                min_value, min_index = box_heights[i], i

        # 만약 최대값-최소값이 1보다 작다면(1,0) 반복을 멈춘다
        if (max_value - min_value) <= 1:
            break
        # 그렇지 않다면 최대값에서 최소값으로 1을 넘겨준다(최댓값은 1감소 최소값은 1증가)
        else:
            box_heights[max_index] -= 1
            box_heights[min_index] += 1
    # 최종 결과를 구해준다. 이때 최종 최댓값과 최종 최솟값을 다시 구해주어 결과를 도출한다
    result = max(box_heights) - min(box_heights)
    print(f"#{t} {result}")