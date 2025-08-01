import json  # JSON 데이터를 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로 처리를 위한 라이브러리


# 1. 파일 경로 설정
# pathlib을 사용하여 파일 경로를 설정합니다.
file_path = Path('data/books_20.json')  # JSON 파일 경로 설정

# 2. 파일 존재 여부 확인
# 파일이 존재하는지 확인하고, 존재하면 파일을 열어 JSON 데이터를 읽습니다.
if file_path.exists():  # 파일이 존재할 경우
    # 파일 열기
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)  # JSON 파일을 파이썬 딕셔너리로 변환하는 코드 (json.load)

    # 3. 정가 범위 분류
    # 도서의 정가를 기준으로 범위를 분류하고, 각 범위에 해당하는 도서 제목을 저장합니다.
    price_categories = {}  # 정가 범위를 저장할 딕셔너리
    price_categories["1만원 이상 2만원 미만"] = []
    price_categories["1만원 미만"] = []
    price_categories["2만원 이상"] = []

    for item in data['item']:  # 'item' 리스트의 각 항목을 순회
        # 정가를 분류하고 해당 범위에 도서 제목을 추가하는 코드
        price_standard = int(item['priceStandard'])
        if price_standard < 10000:
            price_categories['1만원 미만'].append(item['title'])
        elif price_standard >= 20000:
            price_categories['2만원 이상'].append(item['title'])
        else:
            price_categories['1만원 이상 2만원 미만'].append(item['title'])

    # 4. 결과 출력
    # 분류된 정가 범위와 도서 제목을 출력합니다.
    print("정가 범위 분류:")
    for category, books in price_categories.items():  # 범위별 도서 출력
        # 범위와 도서 제목을 출력하는 코드 (print(f"{category}:", books))
        print(category + ':')
        for book in books:
            print(f"  - {book}")
else:
    # 6. 파일이 없을 경우 처리
    # 파일이 존재하지 않으면 오류 메시지를 출력합니다.
    print(f"파일이 존재하지 않습니다: {file_path}")  # 파일이 존재하지 않을 때의 처리 코드 (print(f"파일이 존재하지 않습니다: {file_path}"))
