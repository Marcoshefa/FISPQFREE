from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/home')
def home():
    return 'home'

@app.route('/novo')
def novo_cadastro():
    return 'novo cadastro'

if __name__ == '__main__':
    app.run()
    