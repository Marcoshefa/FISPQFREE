from flask import Flask
from modules.auth.routes import auth_routes
from database import mysql

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'admin01'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Faby162283!'
app.config['MYSQL_DATABASE_DB'] = 'DB_FISPQ'

mysql.init_app(app)

app.register_blueprint(auth_routes)

app.run(host='localhost', port=5000)