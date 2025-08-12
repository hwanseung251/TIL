import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    # 미리 테스트 번호 출력
    print(f"#{t}")
    # 첫번째 줄은 항상 1이므로 출력
    print(1)
    # 첫 번째 줄의 상황을 stack에 넣어놓는다. (단 양옆에 0으로 패딩을 추가)
    stack = [0,1,0]

    # 이미 첫번째는 했으므로 두번째부터 포문돌기
    for i in range(1,N):
        # stack을 재 할당해주기 위한 result스택을 0을 담아서 초기화(첫번째 0패딩)
        result = [0]
        # 만약 스택의 길이가 1이상이면 반복(left와 right pop가능하도록)
        while len(stack) > 1:
            right = stack.pop()
            left = stack.pop()
            result.append(left + right)
            print(left + right, end=' ')
            # left는 재활용되어야 하므로 다시 append해준다
            stack.append(left)
        print()
        # 마지막 0패딩을 해주고
        result.append(0)
        # stack을 다음 단계로 설정해준다
        stack = result

