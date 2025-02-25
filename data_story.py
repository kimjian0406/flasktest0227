# data_store.py

# 책 데이터 저장소
books = []

# 책 추가 함수
def add_book(book):
    books.append(book)

# 책 목록 반환 함수
def get_books():
    return books

# 예시 데이터
if __name__ == "__main__":
    add_book({"id": 1, "title": "Book One", "author": "Author One"})
    add_book({"id": 2, "title": "Book Two", "author": "Author Two"})
    print(get_books())

