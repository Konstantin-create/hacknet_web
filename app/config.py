import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQL_ALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'
    SQL_ALCHEMY_TEACK_MODIFICATIONS = False
