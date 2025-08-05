def restructure_word(word, arr):
    for w in word:
        if w.isdecimal():
            for _ in range(int(w)):
                arr.pop()
        else:
            arr.remove(w)
    return arr
original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

# 변수에 담긴 각 문자열을 모두 나누어 arr에 담는다
arr.extend(original_word)
print(arr)

result = restructure_word(word, arr)
print(result)
print("".join(result))