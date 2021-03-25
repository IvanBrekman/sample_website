import random as rd

from flask import Flask, url_for, request, redirect
from wikipediaapi import Wikipedia

app = Flask(__name__)

alerts = ['primary', 'secondary', 'success', 'danger', 'info', 'light', 'dark']


@app.route('/')
def home():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promo():
    data = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
            'Присоединяйся!']
    return "<br>".join(data)


@app.route('/promotion_image')
def promo_image():
    data = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
            'Присоединяйся!']
    rd.shuffle(alerts)
    return f"""<html>

                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>

                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for('static', filename='img/mars.jpg')}>
                    <br>
                    {''.join([f'<div class="alert alert-{alert}" role="alert">{text}</div>'
                              for text, alert in zip(data, alerts)])}
                  </body>

                </html>
            """


@app.route('/image_mars')
def mars_image():
    return f"""<html>

                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>

                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for('static', filename='img/mars.jpg')}>
                    <br>Вот она какая, красная планета
                  </body>

                </html>
            """


@app.route('/astronaut_selection', methods=["POST", "GET"])
def form():
    if request.method == "GET":
        return f"""
                <!DOCTYPE html>
                <html lang="en">

                <head>
                    <meta charset="UTF-8">
                    <title>Отбор астронавтов</title>
                    <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}" type="text/css" >
                </head>

                <body>
                    <h1>Анкета претендента</h1>
                    <h2>на участие в миссии</h2>

                    <div>
                        <form class="selection-form" method="post" enctype="multipart/form-data">
                            <input class="form-control" type="text" id="surname" name="surname" placeholder="Введите Фамилию" required />
                            <input class="form-control" type="text" id="name" name="name" placeholder="Введите Имя" required />
                            <input class="form-control" type="email" id="email" name="email" placeholder="Введите адрес электронной почты" required />

                            <div class="form-group">
                                <label class="title" for="education">Какое у вас образование?</label>
                                <select class="form-control" id="education" name="education">
                                    <option>Начальное</option>
                                    <option>Среднее</option>
                                    <option>Высшее</option>
                                    <option>Послевузовское</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label class="title" for="profession">Выберите профессию</label>
                                <select class="form-control" id="profession" name="profession">
                                    <option>Инженер-исследователь</option>
                                    <option>Пилот</option>
                                    <option>Строитель</option>
                                    <option>Экзобиолог</option>
                                    <option>Врач</option>
                                    <option>Инженер по терраформированию</option>
                                    <option>Климатолог</option>
                                    <option>Специалист по радиационной защите</option>
                                    <option>Астрогеолог</option>
                                    <option>Гляциолог</option>
                                    <option>Инженер жизнеобеспечения</option>
                                    <option>Метеоролог</option>
                                    <option>Оператор марсохода</option>
                                    <option>Киберинженер</option>
                                    <option>Штурман</option>
                                    <option>Пилот дронов</option>
                                    <option>Командир экспедиции</option>
                                    <option>Научный руководитель</option>
                                </select>
                            </div>
                            <div id="sex" class="form-group">
                                <label class="title" for="sex">Укажите пол</label>

                                <div class="form-check">
                                    <input type="radio" id="male" name="male" checked>
                                    <label class="selected" for="male">Мужской</label>
                                </div>
                                <div class="form-check">
                                    <input type="radio" id="female" name="female">
                                    <label class="selected" for="female">Женский</label>
                                </div>
                            </div>

                            <label class="title" for="motivation">Почему именно Вы должны принять участие в экспедиции на Марс?</label>
                            <textarea class="form-control" id="motivation" name="motivation" rows="3" ></textarea>

                            <label class="title" for="photo">Выберите вашу фотографию</label>
                            <p><input type="file" class="" id="photo" name="photo" accept="image/*" size="10px" required></p>

                            <input type="checkbox" class="form-check-input" id="ready" required>
                            <label class="form-check-label" for="ready" id="ready_label">Я готов ко всем трудностям экспедиции</label>

                            <input type="submit" class="btn btn-primary" />
                        </form>
                    </div>
                </body>

                </html>"""
    elif request.method == "POST":
        data = request.form
        print(data)

        fullname = request.form['surname'] + ' ' + request.form['name']
        email = request.form['email']

        return f"""
                <h2>Здравствуйте, {fullname}!</h2>
                <h3>Мы получили вашу форму и в скором времени обязательно ее рассмотрим</h3>
                <h3>Ожидайте письма от нас на указанную почту: {email}</h3>
                """


@app.route('/choice', methods=["POST", "GET"])
def planet_choice():
    if request.method == "GET":
        return f"""
                <!DOCTYPE html>
                <html lang="en">

                <head>
                    <meta charset="UTF-8">
                    <title>Выбор планеты</title>
                    <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                </head>

                <body>
                    <h1>Выберите планету</h1>
                    <form method="post">
                    <input class="form-control" type="text" id="planet" name="planet" placeholder="Введите название планеты" required />
                    <input type="submit" class="btn btn-primary" />
                    </form>
                </body>

                </html>"""
    elif request.method == "POST":
        planet_name = request.form.get('planet', 'Земля')
        return redirect(f'/choice/{planet_name}')


@app.route('/choice/<planet_name>')
def planet_info(planet_name):
    wiki = Wikipedia('ru')
    page = wiki.page(f'{planet_name}')
    data = page.summary.split('.')[:5]

    rd.shuffle(alerts)

    return f"""
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <title>{planet_name}</title>
            <link rel="stylesheet"
                  href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                  integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                  crossorigin="anonymous">
        </head>

        <body>
            <h1>Я выбираю планету {planet_name}</h1>
            <br><br><br>
            {''.join([f'<div class="alert alert-{alert}" role="alert">{text}</div>'
                      for text, alert in zip(data, alerts)])}
        </body>

        </html>"""


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
