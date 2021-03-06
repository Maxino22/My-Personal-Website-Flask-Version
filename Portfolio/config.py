import os
from datetime import timedelta
import json

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static/images')

with open("/etc/config.json") as config_file:
    config = json.load(config_file)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + \
        os.path.join(BASE_DIR, 'db.sqlite')
    SECRET_KEY = config.get('SECRET_KEY')
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_SALT = 'jnbtrbggtrnhguhtr'
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_SEND_EMAIL = True
    SECURITY_EMAIL_SENDER = config.get('MAIL_USERNAME')
    SECURITY_CONFIRMABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True
    UPLOADED_PHOTOS_DEST = STATIC_ROOT
    SECURITY_POST_LOGIN_VIEW = ('author.admin')
    SECURITY_POST_LOGOUT_VIEW = ('security.login')
    SECURITY_POST_REGISTER_VIEW = '/login'
    SECURITY_POST_CONFIRM_VIEW = '/login'
    SECURITY_EMAIL_PLAINTEXT = False
    SECURITY_EMAIL_HTML = True
    SECURITY_FLASH_MESSAGES = True
    SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED = (
        'This Email is Registered to another account', 'error')
    SECURITY_MSG_USER_DOES_NOT_EXIST = ('This User Does not Exist!', 'error')
    SECURITY_DEFAULT_REMEMBER_ME = True
    DEBUG = True

    # flask ckeditor
    CKEDITOR_HEIGHT = 500
    CKEDITOR_WIDTH = 900
    CKEDITOR_ENABLE_CODESNIPPET = True
    DISCUSSION_DISQUS_SHORTNAME = "maxmuhanda"
    CKEDITOR_CODE_THEME = 'atelier-dune.dark'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = config.get('MAIL_USERNAME')
    MAIL_PASSWORD = config.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = 'ajaybullex@gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False


class ConfigRemote:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://dbadmin:Maxino22@localhost/portfolio'
    SECRET_KEY = config.get('SECRET_KEY')
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_SALT = 'jnbtrbggtrnhguhtr'
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_SEND_EMAIL = True
    SECURITY_EMAIL_SENDER = config.get('MAIL_USERNAME')
    SECURITY_CONFIRMABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_POST_LOGIN_VIEW = ('author.admin')
    SECURITY_POST_LOGOUT_VIEW = ('security.login')
    EMAIL_SUBJECT_REGISTER = 'Verify Your Email To Access'
    SECURITY_POST_REGISTER_VIEW = '/login'
    SECURITY_POST_CONFIRM_VIEW = '/login'
    SECURITY_EMAIL_PLAINTEXT = False
    SECURITY_EMAIL_HTML = True
    SECURITY_FLASH_MESSAGES = True
    SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED = (
        'This Email is Registered to another account', 'error')
    SECURITY_MSG_USER_DOES_NOT_EXIST = ('This User Does not Exist!', 'error')
    SECURITY_DEFAULT_REMEMBER_ME = True
    UPLOADED_PHOTOS_DEST = STATIC_ROOT
    PERMANENT_SESSION_LIFETIME = timedelta(
        minutes=30)

    DEBUG = True

    # flask ckeditor
    CKEDITOR_HEIGHT = 500
    CKEDITOR_WIDTH = 900
    CKEDITOR_ENABLE_CODESNIPPET = True
    CKEDITOR_CODE_THEME = 'atelier-dune.dark'
    #flask discussion
    DISCUSSION_DISQUS_SHORTNAME = "maxmuhanda"
    # mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = config.get('MAIL_USERNAME')
    MAIL_PASSWORD = config.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = 'ajaybullexgmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
