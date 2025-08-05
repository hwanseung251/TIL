# 아래 함수를 수정하시오.
def sort_tuple(tup):

    lst = list(tup)
    lst.sort()
    new_tuple = tuple(lst)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
