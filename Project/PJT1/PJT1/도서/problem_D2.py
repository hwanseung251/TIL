import json
from pathlib import Path
from collections import defaultdict
import statistics

# 1. 파일 경로 설정
file_path = Path('data/books_500.json')

if file_path.exists():
    with file_path.open('r', encoding='utf-8') as file:
        books = json.load(file)

    # 할인율 계산 함수
    def calculate_discount_rate(book):
        """할인율 계산"""
        if book['priceStandard'] == 0:  # 0으로 나누는 에러 방지
            return 0
        return (book['priceStandard'] - book['priceSales']) / book['priceStandard'] * 100

    # 할인율과 판매량 관계 분석
    discount_sales_data = []
    for book in books:
        discount_rate = calculate_discount_rate(book)
        sales_point = book.get('salesPoint', 0)  # 판매량(또는 판매 포인트)
        discount_sales_data.append((discount_rate, sales_point))

    # 평균 할인율 / 평균 판매량
    avg_discount = statistics.mean([d[0] for d in discount_sales_data])
    avg_sales = statistics.mean([d[1] for d in discount_sales_data])

    print("할인율과 판매량 관계")
    print(f"- 전체 평균 할인율: {avg_discount:.2f}%")
    print(f"- 전체 평균 판매량: {avg_sales:.2f}")
    print()

    # 저자별 도서 생산성 분석
    author_books = defaultdict(list)
    for book in books:
        author_books[book['author']].append(book)

    author_stats = []
    for author, authored_books in author_books.items():
        total_books = len(authored_books)
        total_sales = sum(b.get('salesPoint', 0) for b in authored_books)
        avg_sales = total_sales / total_books if total_books else 0
        author_stats.append((author, total_books, avg_sales))

    # 도서 많이 낸 TOP 5 저자
    top_authors = sorted(author_stats, key=lambda x: x[1], reverse=True)[:5]

    print("저자별 도서 생산성 TOP 5 (도서 수 기준)")
    for author, count, avg_sales in top_authors:
        print(f"- {author}: {count}권, 평균 판매량 {avg_sales:.1f}")
    print()

    # 카테고리별 평균 할인율
    category_discount = defaultdict(list)
    for book in books:
        category = book['categoryName']
        discount_rate = calculate_discount_rate(book)
        category_discount[category].append(discount_rate)

    category_avg_discount = [(cat, statistics.mean(rates)) for cat, rates in category_discount.items()]
    top_discount_cats = sorted(category_avg_discount, key=lambda x: x[1], reverse=True)[:5]

    print("카테고리별 평균 할인율 TOP 5")
    for cat, avg_disc in top_discount_cats:
        print(f"- {cat}: 평균 할인율 {avg_disc:.2f}%")

else:
    print(f"파일이 존재하지 않습니다: {file_path}")

'''GPT활용 인사이트
📌 1. 할인율과 판매량 관계
전체 평균 할인율: 10.02%

전체 평균 판매량: 3,418.82권

➡ 해석

전체적으로 도서 할인율은 10% 내외로 낮지만, 판매량 평균이 3,400권 이상이라는 점에서 큰 할인 없이도 팔리는 책들이 많다는 것을 알 수 있음.

할인율이 높다고 반드시 판매량이 높을까?

카테고리별 할인율 TOP 5를 보면 30%까지 할인하는 카테고리도 있지만, 할인율 높은 카테고리가 판매량 TOP 저자와 직접적으로 연결되지 않음.

즉, **콘텐츠 자체의 힘(저자 인지도, 콘텐츠 질)**이 할인율보다 판매량에 더 큰 영향을 줄 가능성이 큼.

✅ 시사점:

책 판매량을 늘리고 싶다면 무조건 할인만 하기보다, 저자 브랜드 강화나 콘텐츠 품질에 더 집중해야 함.

다만 **할인 전략은 특정 카테고리(스티커북, 사운드북 등 유아용)**에서는 효과적일 수 있음.

📌 2. 저자별 도서 생산성 (TOP 5)
1️⃣ 이재범 (지은이) – 16권 / 평균 판매량 510.9권
2️⃣ 홍민정(지은이)·김무연(그림) – 10권 / 평균 판매량 3,537.9권
3️⃣ 홍민정(지은이)·김재희(그림) – 9권 / 평균 판매량 20,347.4권
4️⃣ EBS 편집부 (지은이) – 9권 / 평균 판매량 14,487.3권
5️⃣ 네코마키(지은이)·오경화(옮긴이) – 6권 / 평균 판매량 4,683.8권

➡ 해석

홍민정 작가는 다른 일러스트레이터와 협업할 때마다 판매량 차이가 큼.

김재희와 작업 → 평균 20,347권

김무연과 작업 → 평균 3,538권
👉 그림 작가의 영향력이 판매량에 크게 작용함.

EBS 편집부는 브랜드 파워로 안정적인 판매량을 확보 (평균 14,487권)

이재범은 16권이라는 ‘출간량’ 면에서는 1위지만, 판매량이 적음(평균 510권) → 양보다 질의 문제가 존재.

✅ 시사점:

저자와 일러스트레이터 조합이 판매량에 큰 영향을 미침 → 출판사는 성공 조합을 찾는 것이 중요.

EBS처럼 브랜드 자체가 신뢰도를 주는 경우 별도의 할인 없이도 높은 판매량 가능.

📌 3. 카테고리별 평균 할인율 TOP 5
국내도서>건강/취미>취미기타>기타: 30%

국내도서>유아>놀이책>스티커북: 23.33%

국내도서>유아>놀이책>사운드북/CD북: 15%

국내도서>유아>놀이책>인형놀이/입체북: 13.33%

국내도서>어린이>동화/명작/고전>외국창작동화: 10%

➡ 해석

할인율이 높은 카테고리는 대부분 유아용 책 (스티커북, 사운드북, 인형놀이북).

이런 책은 반복 구매가 많고, 부모들이 여러 개를 사는 경우가 많아 할인 전략이 먹히는 분야.

하지만 이 카테고리들이 저자별 판매량 TOP과 겹치지 않음.

즉, 대량 할인 = 대량 판매 공식이 성립되지 않음.

✅ 시사점:

유아용 카테고리는 할인 전략이 잘 먹히지만, **저자 브랜드가 중요한 분야(동화, 명작, EBS 출판물 등)**는 할인보다 콘텐츠 신뢰도와 브랜드가 더 중요.

🔍 종합 인사이트
1️⃣ 할인율이 판매량에 직접적인 영향을 주지 않음.
→ 출판사는 ‘무조건 할인 전략’보다 브랜드 가치, 저자·일러스트 조합을 통한 판매량 확보가 더 효과적임.

2️⃣ 저자와 협업 파트너(그림 작가, 번역가 등)의 조합이 판매량을 크게 바꿈.
→ **‘작가 케미스트리’**를 전략적으로 관리하면 판매량 상승 가능.

3️⃣ 유아 카테고리는 할인 전략, 학습/명작류는 브랜드 전략으로 구분 필요.
→ 카테고리별 차별화된 판매 전략이 효과적.
'''