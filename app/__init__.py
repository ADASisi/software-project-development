from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop_inventory.db'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  
app.config['SECRET_KEY'] = 'your_flask_login_secret_key'  
db = SQLAlchemy(app)
jwt = JWTManager(app)
login_manager = LoginManager(app)
