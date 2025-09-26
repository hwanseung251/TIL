import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리
from pprint import pprint
# 1. 파일 경로 설정 (books_500.json 사용)
file_path = Path('data/books_500.json')  # 파일 경로 설정 부분

# 파일 존재 여부 확인
if file_path.exists():  # 파일이 존재할 경우
    # 2. 파일 열기
    # 파일을 열고 JSON 데이터를 읽는 코드 (파일 열기, json.load 사용)
    with file_path.open('r', encoding='utf-8') as file:
        books = json.load(file)
    
    # 책의 어른 / 어린이 별로
    # 책의 평균 가격, 카테고리 top 3
    not_child_book = {'평균가격': [0, 0], '카테고리': {}}
    child_book = {'평균가격': [0, 0], '카테고리': {}}

    for book in books:
        price = int(book['priceStandard'])
        category = book['categoryName']

        if '어린이' not in book['categoryName']:
            not_child_book['평균가격'][0] += 1
            not_child_book['평균가격'][1] += price
            
            if category not in not_child_book['카테고리']:
                not_child_book['카테고리'][category] = 0
            not_child_book['카테고리'][category] += 1

        else:
            child_book['평균가격'][0] += 1
            child_book['평균가격'][1] += price
            
            if category not in child_book['카테고리']:
                child_book['카테고리'][category] = 0
            child_book['카테고리'][category] += 1

    # 평균 가격 계산
    not_child_avg = not_child_book['평균가격'][1] / not_child_book['평균가격'][0] if not_child_book['평균가격'][0] > 0 else 0
    child_avg = child_book['평균가격'][1] / child_book['평균가격'][0] if child_book['평균가격'][0] > 0 else 0

    pprint({
        '비어린이 도서 평균 가격': round(not_child_avg, 2),
        '어린이 도서 평균 가격': round(child_avg, 2),
        '비어린이 카테고리 TOP3': sorted(not_child_book['카테고리'].items(), key=lambda x: x[1], reverse=True)[:3],
        '어린이 카테고리 TOP3': sorted(child_book['카테고리'].items(), key=lambda x: x[1], reverse=True)[:3]
    })

else:
    print(f"파일이 존재하지 않습니다: {file_path}")

''' 생성형 AI 요약 요청 결과
📊 데이터 요약

✅ 평균 가격 비교

비어린이 도서 평균 가격: 16,057원

어린이 도서 평균 가격: 14,635원
👉 비어린이 도서가 어린이 도서보다 평균 1,400원가량 더 비쌈.

✅ 카테고리별 TOP3
📚 비어린이 도서

국내도서>유아>그림책>나라별 그림책>한국 그림책 (21권)

국내도서>만화>동물만화 (21권)

국내도서>건강/취미>반려동물 (19권)

📚 어린이 도서

국내도서>어린이>동화/명작/고전>국내창작동화 (63권)

국내도서>어린이>동화/명작/고전>외국창작동화 (20권)

국내도서>어린이>과학/수학/컴퓨터>생물과 생명 (11권)

✅ 핵심 포인트

비어린이 도서: 유아 그림책·만화·반려동물 카테고리 중심 (생활·취미 관련성 높음)

어린이 도서: 동화·명작·고전이 압도적(특히 국내창작동화 비중이 매우 큼)

가격 차이: 어린이 도서는 상대적으로 저렴 → 부모들의 반복 구매 가능성 고려한 가격 전략으로 보임.
'''