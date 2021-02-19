from flask import Flask, request, url_for
import os


app = Flask(__name__)


@app.route('/')
def start_page():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <p>Миссия колонизация Марса</p>
                        </br>
                        <p><a href="/">Стартовая страница</a></p>
                        <p><a href="index">Колонизация Марса</a></p>
                        <p><a href="promotion">Рекламная кампания</a></p>
                        <p><a href="image_mars">Изображение Марса</a></p>
                        <p><a href="promotion_image">Реклама с картинкой</a></p>
                        <p><a href="selection">Отбор астронавтов</a></p>
                        </br>
                        <p>Домашних заданий пока нет(</p>
                        </br>
                        <p><a href="load_photo">Загрузка фотографии</a></p>
                      </body>
                    </html>"""


@app.route('/index')
def index_page():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    promotion_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                      'Присоединяйся!']
    return '</br>'.join(promotion_list)


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="/static/img/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
                        <p>Вот она какая, красная планета.</p>
                      </body>
                    </html>"""


@app.route('/selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <h2 align="center">на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    </br>
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="edu_level">
                                          <option>Дошкольное</option>
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>Послевузовское</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="professions">Какие у вас есть профессии?</label></br>
                                        <input type="checkbox" class="form-check-input" id="engineer-researcher" name="professions">
                                        <label class="form-check-label" for="engineer-researcher">Инженер-исследователь</label></br>

                                        <input type="checkbox" class="form-check-input" id="pilot" name="professions">
                                        <label class="form-check-label" for="pilot">Пилот</label></br>

                                        <input type="checkbox" class="form-check-input" id="builder" name="professions">
                                        <label class="form-check-label" for="builder">Строитель</label></br>

                                        <input type="checkbox" class="form-check-input" id="exobiologist" name="professions">
                                        <label class="form-check-label" for="exobiologist">Экзобиолог</label></br>

                                        <input type="checkbox" class="form-check-input" id="doctor" name="professions">
                                        <label class="form-check-label" for="doctor">Врач</label></br>

                                        <input type="checkbox" class="form-check-input" id="terra-engineer" name="professions">
                                        <label class="form-check-label" for="terra-engineer">Инженер по терраформированию</label></br>

                                        <input type="checkbox" class="form-check-input" id="climatologist" name="professions">
                                        <label class="form-check-label" for="climatologist">Климатолог</label></br>

                                        <input type="checkbox" class="form-check-input" id="radio-engineer" name="professions">
                                        <label class="form-check-label" for="radio-engineer">Специалист по радиационной защите</label></br>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="readyCheck" name="ready">
                                        <label class="form-check-label" for="readyCheck">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['edu_level'])
        print(request.form['professions'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['ready'])
        return "Форма отправлена"


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнём с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form.css')}" />
                            <title>Отбор космонавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h2 align="center">для участия в миссии</h2>
                            <div>
                            <form method="post" class="login_form" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open('image.jpeg', "wb") as file:
            file.write(f.read())
        os.replace('image.jpeg', 'static/img/image.jpeg')
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form.css')}" />
                            <title>Отбор космонавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h2 align="center">для участия в миссии</h2>
                            <form method="post" class="login_form" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <img src="/static/img/image.jpeg" alt="здесь должна была быть картинка, но не нашлась">
                                </br>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
