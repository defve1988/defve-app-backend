from app.extensions import db, ma
from app.utils import data_query
from sqlalchemy.dialects.postgresql import ARRAY, array

# --------------------------------------------------------#
class Timeline(db.Model):
    __tablename__ = "timeline"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20),unique=True, nullable=False)
    content = db.Column(db.Text)
    created = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    tags = db.Column(db.String(100), nullable=False)

    def __init__(self,data):
        data_query.update(self, data)

class TimelineSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Timeline
    id = ma.auto_field()
    title = ma.auto_field()
    content = ma.auto_field()
    created = ma.auto_field()
    color = ma.auto_field()
    tags = ma.auto_field()

# --------------------------------------------------------#
class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),unique=True, nullable=False)
    headline = db.Column(db.Text)
    content = db.Column(db.Text)
    created = db.Column(db.String(20))
    color = db.Column(db.String(20))
    tags = db.Column(db.String(100))

    def __init__(self,data):
        data_query.update(self, data)

class NoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Note
    id = ma.auto_field()
    title = ma.auto_field()
    headline = ma.auto_field()
    content = ma.auto_field()
    created = ma.auto_field()
    color = ma.auto_field()
    tags = ma.auto_field()

# --------------------------------------------------------#
class Todo(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20),unique=True, nullable=False)
    content = db.Column(db.Text)
    start = db.Column(db.String(20))
    due = db.Column(db.String(20))
    completed = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(20))
    tags = db.Column(db.String(100))

    def __init__(self,data):
        data_query.update(self, data)

class TodoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Todo
    id = ma.auto_field()
    title = ma.auto_field()
    content = ma.auto_field()
    start = ma.auto_field()
    due = ma.auto_field()
    completed = ma.auto_field()
    color = ma.auto_field()
    tags = ma.auto_field()

# --------------------------------------------------------#
class FlashCard(db.Model):
    __tablename__ = "flashcard"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),unique=True, nullable=False)
    hint = db.Column(db.Text)
    back_content = db.Column(db.Text, nullable=False)
    created = db.Column(db.String(20))
    rate = db.Column(db.String(20))
    tags = db.Column(db.String(100))

    def __init__(self,data):
        data_query.update(self, data)

class FlashCardSchema(ma.SQLAlchemySchema):
    class Meta:
        model = FlashCard
    id = ma.auto_field()
    title = ma.auto_field()
    hint = ma.auto_field()
    back_content = ma.auto_field()
    created = ma.auto_field()
    rate = ma.auto_field()
    tags = ma.auto_field()