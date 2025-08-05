def rental_book(대여자_이름, 대여_책수):
    decrease_book(대여_책수)
    print(f'{대여자_이름}님이 {대여_책수}권의 책을 대여하였습니다.')

number_of_book = 100

def decrease_book(대여_책수):
    global number_of_book
    number_of_book -= 대여_책수
    print(f'남은 책의 수 : {number_of_book}' )

rental_book('홍길동', 3)