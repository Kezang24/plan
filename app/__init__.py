import imp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import engine
from sqlalchemy.engine import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_cors import CORS

#set db connection
db_connection = f"mysql+pymysql://root:root@127.0.0.1:3306/crud"
#configure the flask app 
app = Flask(__name__)

# set your config properties BEFORE passing the app to SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = db_connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app configure
db = SQLAlchemy(app)

#connecting to database ..
engine = create_engine(db_connection, echo=True)

if not database_exists(engine.url):
    create_database(engine.url)
else:
    engine.connect()
    
from app.controller import all_operation
from app.Model import database
# db.create_all()





