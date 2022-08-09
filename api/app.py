from flask import Flask
from modules.auth.routes import auth_routes
from database import mysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Marcos21111984!'
app.config['MYSQL_DATABASE_DB'] = 'DB_FISPQ'

mysql.init_app(app)

app.register_blueprint(auth_routes)

app.run(host='localhost', port=5000)