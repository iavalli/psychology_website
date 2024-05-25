
app.route('/blog')
def blog():
    response = make_response('Блог')
    # Устанавливаем заголовок
    response.headers['Блог'] = 'Статьи по психологии'
    # Меняем тип ответа
    response.mimetype = 'text/plain'
    # Задаем статус
    response.status_code = 418
    # Устанавливаем cookie
    response.set_cookie('foo', 'bar')
    return response



from flask import Flask, jsonify, request

from data import generate_companies

companies = generate_companies(100)

app = Flask(__name__)

###

@app.route('/')
def index():
    return "<a href='/companies'>Companies</a>"


# BEGIN (write your solution here)
@app.route('/companies')
def get_companies():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('per', 5, type=int)
    offset = (page - 1) * limit
    slice_of_companies = companies[offset:page*limit]
    return jsonify(slice_of_companies)

##

@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'
curl localhost:8000/courses/132

Course id: 132

##

