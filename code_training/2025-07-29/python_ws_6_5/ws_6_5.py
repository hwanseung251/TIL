def ordered_difference_sets(set1, set2):
    result_left = set1 - set2
    result_right = set2 - set1
    if len(result_left) > len(result_right):
        return result_right, result_left
    else:
        return result_left, result_right
# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
