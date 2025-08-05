import sys
sys.stdin = open("input.txt")

T = int(input())

def one_count(num_index):
    """
    호출되면 그 시작점부터 연속된 1을 카운팅해주는 함수
    return 연속된 1의 개수
    """
    cnt = 0
    # 지금 위치에 값이 1이고
    while num_sequence[num_index] == '1':
        # 아직 지나지 않은 1이라면
        chk[num_index] = True
        # 개수를 1더해주고, 인덱스도 앞으로 전진해줌
        cnt += 1
        num_index += 1
        # 인덱스를 전진했을때 N이상이면 멈춘다
        if num_index >= N:
            break
    return cnt

for t in range(1, T+1):
    N = int(input())
    num_sequence = input()
    # 1이 체크된 1인지 체크해주는 체크 박스 생성
    chk = [False] * N
    # 최대 개수를 저장해줄 변수 생성
    max_value = 0

    for i in range(N):
        # 만약 지금 위치에서 1이고 아직 지나지 않은 1이라면 1의 시작점이므로 만들어논 함수 호출
        if (num_sequence[i] == '1') and (chk[i] == False):
            # 함수 반환값으로 얻은 값과 현재 최대값을 비교해 갱신해준다
            max_value = max(max_value, one_count(i))

    print(f"#{t} {max_value}")