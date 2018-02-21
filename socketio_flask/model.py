from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class User_lista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lista = db.Column(db.String(120000), unique=False, nullable=False)


"""
from model import db
db.create_all()
from model import User_lista
db.session.add(User_lista(lista = "['hola', 'que tal']"))
db.session.commit()


from model import User_lista, db
lista = User_lista.query.filter_by(id=1).first()
db.session.commit()
 """