# from flask import Flask, request, jsonify
# from database import TestDB, test_schema
# from app import app, db
# from func import *

# @app.route('/get',methods=['GET'])
# def get_test():
#     u ='https://www.youtube.com/watch?v=gyBkHYWNsv4'
#     title, url = video_title(u)
#     res = {"title":title,
#             "url":url}
#     return jsonify(res)

# @app.route('/add',methods=['POST'])
# def add_test():
#     new_data = TestDB(request.json)
#     db.session.add(new_data)
#     db.session.commit()
#     res = test_schema.dump([new_data])
#     return jsonify(res)

# @app.route('/get2',methods=['GET'])
# def get_test2():
#     data_all = TestDB.query.all()
#     res = test_schema.dump(data_all)
#     return jsonify(res)

from app.utils import video_title