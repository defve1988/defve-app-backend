import os 

data_dir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(data_dir,'app_db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False