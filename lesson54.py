from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Главная</h1>
    <p>Добро пожаловать</p>
    <a href='/about'>О мне</a>
    <a href='/cat'>Котик</a>
    """

@app.route('/about')
def about():
    return """
    <h1>О мне</h1>
    <p>Это мой первый сайтик но он имеет крутую функцию он показывает рандомного кота</p>
    <a href='/'>Главная</a>
    """

@app.route('/cat')
def get_cat():
    return """
    <h1>Случайный котик</h1>
    <img src='https://cataas.com/cat' width='300'>
    <br>
    <a href='/'>Главная</a>
    """

if __name__ == '__main__':  
    app.run(debug=True)