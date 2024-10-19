# test_config.py
import os

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://logginapp:LogginApp123@localhost/userauthenticator_test')
    SECRET_KEY = os.getenv('SECRET_KEY', 'tu_clave_secreta')
    SQLALCHEMY_TRACK_MODIFICATIONS = True