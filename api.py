from flask import Flask, jsonify, request

app = Flask(__name__)

# 샘플 책 데이터
books = [
    {"id": 1, "title": "책 제목 1", "author": "저자 1"},
    {"id": 2, "title": "책 제목 2", "author": "저자 2"},
    {"id": 3, "title": "책 제목 3", "author": "저자 3"},
]

# GET 엔드포인트: 책 목록 보여주기
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# POST 엔드포인트: 새 책 추가하기
@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.json  # 요청 본문에서 JSON 데이터 가져오기
    new_book['id'] = len(books) + 1  # 새로운 책 ID 생성
    books.append(new_book)  # 리스트에 새 책 추가
    return jsonify(new_book), 201  # 추가된 책을 반환하고 201 Created 상태 코드 반환

if __name__ == '__main__':
    app.run(debug=True)

