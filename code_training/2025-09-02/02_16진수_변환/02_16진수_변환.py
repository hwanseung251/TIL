import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(1, T+1):
    x_num = input().strip()

    # 16진수 각 자리 -> 4비트 이진수로 보존해 이어붙이기
    bitstream = ''.join(format(int(h, 16), '04b') for h in x_num)
    buf = ''
    out = []

    # 비트를 한 자리씩 버퍼에 쌓으면서 앞에서 7비트씩 처리
    for b in bitstream:
        buf += b
        # 버퍼에 7비트 이상 있으면 가능한 만큼 반복 처리
        while len(buf) >= 7:
            chunk7 = buf[:7]
            if chunk7 == '0000000':
                # 규칙: 앞 4비트 버리고 뒤 3비트는 다음과 합침
                buf = buf[4:]   # (앞 4비트만 제거)
            else:
                out.append(str(int(chunk7, 2)))
                buf = buf[7:]   # 정상적으로 7비트 소비

    # 남은 비트가 있으면(7 미만) 그대로 10진수로 출력
    if buf:
        out.append(str(int(buf, 2)))

    print(f"#{t} {' '.join(out)}")
