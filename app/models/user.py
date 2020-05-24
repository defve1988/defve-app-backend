from app.extensions import db, ma
from app.utils import data_query

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique=True, nullable=False)
    pwd = db.Column(db.String(20), nullable=False)
    level = db.Column(db.String(10), nullable=False)
    created = db.Column(db.String(20))

    def __init__(self,data):
        data_query.update(self, data)

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
    id = ma.auto_field()
    name = ma.auto_field()
    # pwd = ma.auto_field()
    level = ma.auto_field()
    created = ma.auto_field()
