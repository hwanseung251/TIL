# arr = ['Fish', 'And', 'Chips']
# # N = len(arr)
# #
# # for i in range(1<<N):
# #     for j in range(N):
# #         if i & (1<<j):
# #             print(arr[j], end =' ')
# #     print()
# N = 10
# for i in range(1<<N):
#     for j in range(N):
#         if i & (1<<j):
#             print(f'{i}번 째 경우의 수 {bin(i)[2:]:0>4} {j}번 째 요소 == {arr[j]}')
#             print(f'1을 {j}번 쉬프트 {bin(1 << j)[2:]:0>4}')
#             print(arr[j])
#     print()
#     print()

nums = [3, 6, 7, 1, 5, 4]

# 해당 리스트의 길이
n = len(nums)

# 부분집합의 개수를 더해 갈 변수 초기화
cnt = 0

# n번 시프트를 통해 모든 경우의 수를 체크하자 -> 2^6 -> 64
for i in range(1 << n):
		cnt += 1
		for j in range(n):
				if i & (1<<j):
						print(nums[j], end=', ')
		print()
print(cnt)