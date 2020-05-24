from flask import Flask
from flask_cors import CORS

from .extensions import db, api, ma

from .models.user import User
from .models.note import Timeline
# , Note, FlashCard, Todo

from .apis.user_api import *
from .apis.note_api import *

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    CORS(app)

    with app.app_context():
        db.create_all()
        print('database created.')

    @app.route('/')
    def return_home():
        return "This is Defve-app's backend."

    return app