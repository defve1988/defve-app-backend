from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def return_home():
    return "This is Defve-app's backend."

if __name__=='__main__':
    app.run()