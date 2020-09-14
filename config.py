import os
basedir = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig:
    DEBUG=True
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345678900987654321'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
