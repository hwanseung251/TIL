new_book = {
  "adult": False,
  "author": "김하늘 (지은이), 박서준 (그림)",
  "categoryId": 51234,
  "categoryName": "국내도서>소설/시/희곡>에세이>힐링에세이",
  "cover": "https://image.example.com/product/00000/00/coversum/fakecover_1.jpg",
  "customerReviewRank": 9,
  "description": "하루하루 지친 마음을 따뜻하게 위로해주는 힐링 에세이. 작가의 소소한 일상 이야기와 함께 독자의 감정을 어루만지는 글들이 담겨 있다.",
  "fixedPrice": True,
  "isbn": "K999999999",
  "isbn13": "9791234567890",
  "itemId": 999999999,
  "link": "http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=999999999&partner=openAPI&start=api",
  "mallType": "BOOK",
  "mileage": 800,
  "priceSales": 14400,
  "priceStandard": 16000,
  "pubDate": "2025-07-25",
  "publisher": "마음숲",
  "salesPoint": 120,
  "seriesInfo": {
    "seriesId": 223344,
    "seriesLink": "http://www.aladin.co.kr/shop/common/wseriesitem.aspx?SRID=223344&partner=openAPI",
    "seriesName": "마음을 쓰다 시리즈"
  },
  "stockStatus": "",
  "subInfo": {},
  "title": "별빛 아래에서 쓰는 편지"
}

import json

with open("new_book.json", "w", encoding="utf-8") as f:
    json.dump(new_book, f, ensure_ascii=False, indent=4)