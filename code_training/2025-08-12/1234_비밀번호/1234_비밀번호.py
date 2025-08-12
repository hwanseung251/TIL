import sys
sys.stdin = open("input.txt")

for t in range(1, 11):
    N, numbers = input().split()
    stack = []

    # 숫자를 하나씩돌면서
    for num in numbers:
        # 지금 스택에 값이 없으면 추가
        if len(stack) == 0:
            stack.append(num)
        else:
            # 값이 있으면 중복검사를하고 중복이면 삭제, 아니면 다시 추가
            pop_item = stack.pop()
            if pop_item != num:
                stack.extend((pop_item, num))

    print(f"#{t} {''.join(stack)}")