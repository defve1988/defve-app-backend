import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from do import *


app = Flask(__name__)
CORS(app)


data_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(data_dir,'app_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class TestDB(db.Model):
    __tablename__ = "test_db"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(500))

    def __init__(self,data):
        self.update(data)
    
    def update(self,data):
        if 'title' in data:
            self.title = data['title']
        if 'content' in data:
            self.content = data['content']

class TestDBSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TestDB
    id = ma.auto_field()
    title = ma.auto_field()
    content = ma.auto_field()

test_schema = TestDBSchema(many = True)

@app.route('/')
def return_home():
    return "This is Defve-app's backend."

@app.route('/get',methods=['GET'])
def get_test():
    u ='https://www.youtube.com/watch?v=gyBkHYWNsv4'
    title, url = video_title(u)
    res = {"title":title,
            "url":url}
    return jsonify(res)

@app.route('/add',methods=['POST'])
def add_test():
    new_data = TestDB(request.json)
    db.session.add(new_data)
    db.session.commit()
    res = test_schema.dump([new_data])
    return jsonify(res)

@app.route('/get2',methods=['GET'])
def get_test2():
    data_all = TestDB.query.all()
    res = test_schema.dump(data_all)
    return jsonify(res)



if __name__=='__main__':
    app.run()