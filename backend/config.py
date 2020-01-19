import logging

class LocalConfig:
    HOST = '0.0.0.0'
    PORT = 5000
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_NAME = 'test_db'
    SQLALCHEMY_DATABASE_URI = f"postgresql://localhost/{SQLALCHEMY_DATABASE_NAME}"
    @classmethod
    def init_app(cls, app):
        app.logger.setLevel(logging.DEBUG)


config_dict = {
    'local': LocalConfig,
}