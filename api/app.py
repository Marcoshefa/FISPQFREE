from flask import Flask
from modules.auth.routes import auth_routes

app = Flask(__name__)

app.register_blueprint(auth_routes)

app.run(host='localhost', port=5000)