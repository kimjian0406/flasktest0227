from flask import Flask, jsonify, request
from marshmallow import Schema, fields

app = Flask(__name__)

# 책 스키마 정의
class BookSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)

# 메모리에 저장할 책 목록
books = []

# 책 목록을 보여주는 GET 엔드포인트
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

if __name__ == '__main__':
    app.run(debug=True)

