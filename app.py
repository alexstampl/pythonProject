from flask import Flask, render_template # render_template (для работы с шаблонами из папки templates)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Используем базу данных SQLITE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pythonProject.db'
db = SQLAlchemy(app)


# Объявим таблицу и создадим колоночки
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(300), nullable=False) # nullable - обязательно к заполнению
    text = db.Column(db.Text, nullable=False)



# Добавляем обработчик (как будут отображаться ссылки)
@app.route('/index')
@app.route('/')
# Главная страница
def index():
    return render_template('index.html')

# О нас
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

