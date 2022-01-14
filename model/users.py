from model import db


class Users(db.Model):
    userId = db.Column(db.String(45), primary_key=True,nullable=False)
    username =  db.Column(db.String(45), nullable=False)
    contact =  db.Column(db.Integer, nullable=False,unique=True)
    