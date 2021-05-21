from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


import sys
sys.path.append(".")



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/sefi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your secret key'




db = SQLAlchemy(app)
migrate = Migrate(app, db)


engine = create_engine('mysql+pymysql://root:@localhost/sefi')
Session = sessionmaker(bind=engine)
session = Session()

from app.controllers.proyectController import  sefi_Route
app.register_blueprint(sefi_Route, url_prefix='/')