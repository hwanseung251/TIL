def itoa(integer_value):
    '''
    itoa 함수: 주어진 정수(integer_value)를 문자열로 변환하여 반환.
    (str() 함수 사용 불가)

    구현 아이디어:
    1) 먼저 0인지, 음수인지 판별 (음수라면 양수로 바꿔 처리, 마지막에 '-' 붙임)
    2) 10으로 나눈 나머지를 이용해 일의 자리부터 문자를 추출 (chr(48 + 나머지))
    3) 반복문으로 몫(// 10)을 업데이트하면서 계속 앞에 문자를 붙임
    4) 모두 끝난 뒤 음수이면 '-'를 앞에 붙임
    5) 0이 입력된 경우 예외처리
    '''
    # 1. 0 처리
    if integer_value == 0:
        return '0'

    # 2. 음수 판별
    is_negative = (integer_value < 0)
    if is_negative:
        integer_value = -integer_value  # 양수로 바꿔서 처리

    # 3. 나머지를 문자로 바꿔 누적
    result_str = ''
    while integer_value > 0:
        remainder = integer_value % 10  # 일의 자리 추출
        # remainder가 5면 chr(48+5) = chr(53) => '5'
        result_str = chr(48 + remainder) + result_str
        integer_value //= 10  # 10으로 나눈 몫을 다음 반복에서 진행

    # 4. 음수면 '-' 붙이기
    if is_negative:
        result_str = '-' + result_str

    return result_str

# --------------------
import sys
sys.stdin = open("input.txt")

T = int(input())
for i in range(1, T + 1):
    number = int(input())  # 변환할 정수
    result = itoa(number)   # str()이 아닌 itoa() 함수로 문자열 변환
    print(f'#{i} {result}', type(result))