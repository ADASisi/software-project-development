from flask import Flask
from flask_restful import Api
from app.controllers.tasks import tasks_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)
db = SQLAlchemy(app)

app.register_blueprint(tasks_bp, url_prefix='/api/v1')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
