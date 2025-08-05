# 아래 함수를 수정하시오.
def even_elements(lst):
    new_lst = []
    for i in lst:
        if i % 2 == 0:
            new_lst.extend([lst.pop(lst.index(i))])

    return new_lst

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
