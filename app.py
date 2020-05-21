from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def return_home():
    return "This is Defve-app's backend."


app.run()