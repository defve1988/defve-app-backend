from flask import request, jsonify
from flask_restful import Resource, abort
from app.extensions import api,db, KEY
from app.models.user import User, UserSchema

user_schema = UserSchema(many = True)

class UserAPI(Resource):
    def get(self):
        try:
            if request.json['key'] == KEY:
                users = User.query.all()
                res = user_schema.dump(users)
                return jsonify(res)
        except:
            abort(404, message="Not authorized.")


    def put(self):
        try:
            if request.json['key'] == KEY:
                new_data = User(request.json)
                db.session.add(new_data)
                db.session.commit()
                res = user_schema.dump([new_data])
                return jsonify(res)
        except:
            abort(404, message="Can't add new user.")

    def post(self):
        res = {'user':'', 'login':'false', 'level':''}
        if len(request.json)>0:
            user = User.query.filter_by(**request.json).first()
            if user:
                res['user'] = user.name
                res['login'] = 'true'
                res['level'] = user.level
        return jsonify(res)

    def delete(self):
        try:
            if request.json['key'] == KEY:
                name = request.json['name']
                data = User.query.filter_by(name=name).first()
                if data and data.pwd == request.json['pwd']:
                    db.session.delete(data)
                    db.session.commit()
                    res = user_schema.dump([data])
                    return jsonify(res)
        except:
            abort(404, message="Can't delete user.")

api.add_resource(UserAPI, '/api/users', endpoint = 'users')