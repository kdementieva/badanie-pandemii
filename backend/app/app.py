from flask import Flask
from models import db

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:start@mariadb:3306/PandemicFeedback'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['RESTFUL_JSON'] = { 'ensure_ascii': False }


  db.init_app(app)
  return app
