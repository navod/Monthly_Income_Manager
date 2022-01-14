from model import db

class Whishlist(db.Model):
    whishId = db.Column(db.String(45), primary_key=True)
    description =  db.Column(db.String(45), nullable=False)
    saveTo =  db.Column(db.Float, nullable=False)
    color =  db.Column(db.String(45), nullable=False)
    saveType =  db.Column(db.String(45), nullable=False)
    startSaveDate =   db.Column(db.String(45), nullable=False)
    
