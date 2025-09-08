import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 카테고리 데이터를 뽑아 JSON파일로 만들기
# 아래에 생성형 AI를 활용한 코드 작성

# 파일 path 받아오기
file_path = Path('data/books_2000.json')

# 카테고리별 도서 분류 딕셔너리 (key: (categoryId, categoryName))
category_books = {}

# 파일 경로가 존재하면
if file_path.exists():
    with file_path.open('r', encoding='utf-8') as file:
        books = json.load(file)

    # 카테고리별로 도서 분류
    for book in books:
        category_id = str(book.get('categoryId'))
        category_name = book.get('categoryName')

        # category_books에 카테고리 최초 저장
        if category_id not in category_books:
            category_books[category_id] = {
                "name": category_name,
                "books": []
                }
            
        # 카테고리 별로 도서 정보 저장
        category_books[category_id]["books"].append({
            'title': book['title'],
            'author': book['author'],
            'publisher': book['publisher'],
            'pubDate': book['pubDate'],
            'isbn': book['isbn13'],
            'price': book['priceSales']
            })
        
    # json 파일로 저장하기
    file_name = 'category_books.json'
    with open(file_name, 'w', encoding='utf-8') as make_file:
        json.dump(category_books, make_file, ensure_ascii=False, indent=2)

    print("JSON 파일이 생성되었습니다: " + file_name) # 파일 생성 문구 출력
else:
    print(f"파일이 존재하지 않습니다: {file_path}")