# 사과는 영어로 apple
# 바나나는 영어로 banana
# 키위는 영어로 kiwi

a = "사과는 영어로 apple "
apple_kr = a[:2]
english = a[4:6]
apple = a[8:]
banana = 'banana'
kiwi = 'kiwi'
banana_kr = '바나나'
kiwi_kr = '키위'
nn = a[2]
ro = a[6]

print(apple_kr + nn + ' ' + english + ro + ' ' + apple)
print(banana_kr + nn + ' ' + english + ro + ' ' + banana)
print(apple_kr + nn + ' ' + english + ro + ' ' + kiwi)