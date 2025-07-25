import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 시리즈 정보가 있는 책들 끼리 묶기
# 아래에 생성형 AI를 활용한 코드 작성

# 파일 path 받아오기
file_path = Path('data/books_500.json')
output_path = Path('series.json')

# 시리즈 딕셔너리: key = seriesId (문자열), value = 시리즈 정보와 책 리스트
series_dict = {}

# 파일 경로가 존재하면
if file_path.exists():
    with file_path.open('r', encoding='utf-8') as file:
        books = json.load(file)

    for book in books:
        series_info = book.get('seriesInfo', None)

        # 시리즈 정보가 있는 경우만 처리
        if series_info:
            series_id = str(series_info.get('seriesId'))
            series_name = series_info.get('seriesName')

            # 시리즈 딕셔너리에 없으면 초기화
            if series_id not in series_dict:
                series_dict[series_id] = {
                    "seriesId": int(series_id),
                    "seriesName": series_name,
                    "books": []
                }

            # 책 정보 추가
            series_dict[series_id]["books"].append({
                "title": book.get("title", ""),
                "link": book.get("link", ""),
                "author": book.get("author", ""),
                "pubDate": book.get("pubDate", ""),
                "description": book.get("description", ""),
                "isbn": book.get("isbn", ""),
                "isbn13": book.get("isbn13", "")
            })

    # 병합된 시리즈 정보 JSON으로 저장
    with output_path.open('w', encoding='utf-8') as f:
        json.dump(series_dict, f, ensure_ascii=False, indent=4)

    # 콘솔 출력
    print("모든 시리즈 데이터가 series.json 파일로 병합되었습니다.")

else:
    print(f"❗ 파일이 존재하지 않습니다: {file_path}")