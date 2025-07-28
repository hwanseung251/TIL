from datetime import datetime  # 날짜와 시간을 처리하기 위한 라이브러리
import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리
from collections import defaultdict
from statistics import mean

# 월별 책 정보 모아보고 평균 가격 계산하기
# 아래에 전체 코드 작성

# 파일 path 받아오기
file_path = Path('data/books_2000.json')

# 월별 도서 정보를 저장할 딕셔너리 (key: YYYY-MM)
monthly_books = defaultdict(list)

# 파일이 존재할 경우
if file_path.exists():
    with file_path.open('r', encoding='utf-8') as file:
        books = json.load(file)

    # 도서를 월별로 분류
    for book in books:
        try:
            pub_date = datetime.strptime(book['pubDate'], "%Y-%m-%d")
            year_month = pub_date.strftime("%m")  # MM 형식으로
            monthly_books[year_month].append(book)
        except Exception as e:
            print(f"날짜 파싱 에러: {book.get('title', '제목없음')} - {e}")

    # 월별 통계 출력
    print("월별 평균 가격 및 도서 수:")
    for month, books_in_month in sorted(monthly_books.items()):
        titles = [book['title'] for book in books_in_month]
        prices = [book['priceSales'] for book in books_in_month if isinstance(book['priceSales'], (int, float))]
        avg_price = round(mean(prices), 2) if prices else 0
        print(f"{int(month)}월: 평균 가격 {avg_price:.2f}원 (총 {len(titles)}권)")
else:
    print(f"파일이 존재하지 않습니다: {file_path}")
