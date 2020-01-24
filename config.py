import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'SECRET_KEY'
