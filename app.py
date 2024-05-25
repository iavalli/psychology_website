from flask import Flask, render_template, make_response


app = Flask(__name__)


@app.get('/')
def get_main():
    return render_template("base.html", title="Main page")


@app.get('/services')
def get_services():
    return render_template("base.html", title="Услуги")


@app.get('/contacts')
def get_contacts():
    return render_template("base.html", title="Контакты")


@app.get('/reviews')
def get_reviews():
    return render_template("base.html", title="Отзывы")


@app.errorhandler(404)
def not_found(error):
    return 'Страница не найдена', 404




"""
/blog
get
get_sorted
post
"""

if __name__ == "__main__":
    app.run(debug=True)
