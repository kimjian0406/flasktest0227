# 책 데이터를 저장할 리스트
books = []

# 책 추가 함수
def add_book(book):
    books.append(book)

# 책 목록 가져오기 함수
def get_books():
    return books

# 책 정보 업데이트 함수
def update_book(book_id, updated_info):
    for book in books:
        if book['id'] == book_id:
            book.update(updated_info)
            return book
    return None

# 책 삭제 함수
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]

# 예시 사용
add_book({'id': 1, 'title': 'Book One', 'author': 'Author One'})
add_book({'id': 2, 'title': 'Book Two', 'author': 'Author Two'})

print(get_books())  # [{'id': 1, 'title': 'Book One', 'author': 'Author One'}, {'id': 2, 'title': 'Book Two', 'author': 'Author Two'}]

update_book(1, {'title': 'Updated Book One'})
print(get_books())  # [{'id': 1, 'title': 'Updated Book One', 'author': 'Author One'}, {'id': 2, 'title': 'Book Two', 'author': 'Author Two'}]

delete_book(2)
print(get_books())  # [{'id': 1, 'title': 'Updated Book One', 'author': 'Author One'}]

