from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

app.route('/hello')
def hello():
    return 'Hello, world'

@app.route('/teste')
def teste():
    return 'Página de teste do html'

@app.route('/about')
def about():
    return 'Tha about page'


