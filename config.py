import os


class Config(object):
    TESTING = False
    SECRET_KEY = 'T5k2NPsjxC4h77ZPbIKYPg4dW2GQN0X1'
    UPLOAD_FOLDER = '/home/jeancarlos/learning/carros/app/static/img'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@localhost:5432/findr'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config = {
 'development': DevelopmentConfig,
 'testing': TestingConfig,
 'production': ProductionConfig,
 
 'default': DevelopmentConfig
}