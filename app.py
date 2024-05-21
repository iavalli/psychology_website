from flask import Flask, render_template


app = Flask(__name__)


@app.get('/')
def get_main():
    return render_template("base.html", title="Main page")


@app.get('/services')
def get_services():
    return "Услуги"


@app.get('/contacts')
def get_contacts():
    return "Контакты"


@app.get('/reviews')
def get_reviews():
    return "Отзывы"


"""
/blog
get
get_sorted
post
"""

if __name__ == "__main__":
    app.run(debug=True)
