from model import db

class WhishListDetail(db.Model):
    __tablename__ = 'whishlistDetail'
    whishDetailId =db.Column(db.Integer, primary_key=True,autoincrement=True)
    whishId =db.Column(db.String(45),db.ForeignKey('whishlist.whishId'))
    userId =db.Column(db.String(45),db.ForeignKey('users.userId'))
    savedAmount= db.Column(db.Float, nullable=False)
    savedDate = db.Column(db.String(45), nullable=False)