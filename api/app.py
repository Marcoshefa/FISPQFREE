import os
from flask import Flask
from modules.auth.routes import auth_routes
from modules.user.routes import user_routes
from modules.fispq.routes import fispq_routes
from database import mysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST', 'localhost')
app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('MYSQL_DATABASE_PORT', '3306'))
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER', 'root')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD', 'Marcos21111984!')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB', 'db_fispq')

# app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST', 'localhost')
# app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('MYSQL_DATABASE_PORT', '3307'))
# app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER', 'root')
# app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD', 'server')
# app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB', 'db_fispq')

mysql.init_app(app)

app.register_blueprint(auth_routes)
app.register_blueprint(user_routes)
app.register_blueprint(fispq_routes)

app.run(host='localhost', port=5000)