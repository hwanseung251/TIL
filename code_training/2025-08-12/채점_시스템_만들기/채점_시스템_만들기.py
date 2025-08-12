import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    # 정답
    ans = list(map(int, input().split()))
    # 학생들의 최댓값과 최솟값 점수를 저장할 변수 각각 생성
    student_score_max = 0
    student_score_min = float('inf')
    # 학생별로 포문돌기
    for i in range(N):
        # 학생의 답안
        student_ans = list(map(int, input().split()))
        # 연속한 정답을 카운팅
        cnt = 0
        # 학생의 최종 스코어 저장 변수
        score = 0
        for m in range(M):
            if ans[m] == student_ans[m]:
                # 정답인경우 연속 카운팅
                cnt += 1
                # 연속한 경우 점수 카운팅
                score += cnt
            else:
                cnt = 0

        # 최댓값 최솟값 갱신
        student_score_max = max(student_score_max, score)
        student_score_min = min(student_score_min, score)

    print(f"#{t} {student_score_max-student_score_min}")