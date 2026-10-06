from flask import Flask, render_template
# render_template (для работы с шаблонами из папки templates)

app = Flask(__name__)

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

