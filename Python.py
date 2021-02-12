from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def start_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index_page():
    return 'И на Марсе будут яблони цвести!'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')