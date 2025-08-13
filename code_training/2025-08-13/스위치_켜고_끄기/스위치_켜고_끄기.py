import sys
sys.stdin = open("input.txt")

switch_num = int(input())
# 0번 인덱스는 사용하지 않는다
switch = [0] + list(map(int, input().split()))
student_num = int(input())

for i in range(student_num):
    gender, num = map(int, input().split())
    # 성별이 남성이면
    if gender == 1:
        K = num
        # 인덱스가 초과하지 않으면 배수 만큼 계속 스위치 상태를 변경한다
        while K < switch_num+1:
            if switch[K] == 0:
                switch[K] += 1
            else:
                switch[K] -= 1
            K += num
    else:
        # 여셩이면 자기 자신은 항상 대칭이므로 바꿀 리스트에 먼저 추가하며 초기화
        change_list = [num]
        d = 1
        # 한칸씩 대칭이동 하면서 범위내에 있으면
        while (num + d) < switch_num+1 and (num - d) >= 1:
            # 대칭을 확인하고 서로 대칭이면 바꿀 리스트에 추가해준다
            if switch[num + d] == switch[num - d]:
                change_list.extend((num+d, num-d))
                d += 1
            else:
                break
        # 바꿀리스트에 있는 스위치들의 상태를 모두 변경해준다
        for number in change_list:
            if switch[number] == 0:
                switch[number] += 1
            else:
                switch[number] -= 1
# 맨앞에 사용하지 않는 0번인덱스 제외하고 출력
for start in range(1, switch_num + 1, 20):
    print(" ".join(map(str, switch[start:min(start + 20, switch_num + 1)])))