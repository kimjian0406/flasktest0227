from flask import Flask, jsonify, request

app = Flask(__name__)

# 예시 데이터
books = [
    {'id': 1, 'title': 'Book One', 'author': 'Author A'},
    {'id': 2, 'title': 'Book Two', 'author': 'Author B'}
]

# 책 목록을 보여주는 GET 엔드포인트
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

# 새 책을 추가하는 POST 엔드포인트
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# 특정 책의 정보를 업데이트하는 PUT 엔드포인트
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])
    return jsonify(book), 200

# 특정 책을 삭제하는 DELETE 엔드포인트
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)

