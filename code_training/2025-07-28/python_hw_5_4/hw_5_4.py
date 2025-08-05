# 아래 함수를 수정하시오.
def find_min_max(lst):
    min_value = min(lst)
    max_value = max(lst)
    return min_value, max_value

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
