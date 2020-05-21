from flask import Flask, request, jsonify

from do import *

app = Flask(__name__)


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

if __name__=='__main__':
    app.run()