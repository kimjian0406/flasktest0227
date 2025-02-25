python hello.py

from flask import Flask
from flask_smorest import Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello():
    return "안녕하세요, Flask 애플리케이션이 실행 중입니다!"

if __name__ == '__main__':
    app.run(debug=True)


