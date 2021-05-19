import os
from datetime import timedelta

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static/images')


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://max:password@localhost/portfolio'
    SECRET_KEY = 'mintjtnrtjnbjt'
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_SALT = 'jnbtrbggtrnhguhtr'
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_SEND_EMAIL = True
    SECURITY_EMAIL_SENDER = 'ajaybullec@gmail.com'
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
    CKEDITOR_CODE_THEME = 'atelier-dune.dark'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = 'ajaybullec@gmail.com'
    MAIL_PASSWORD = 'tlulkqxzyedrkvus'
    MAIL_DEFAULT_SENDER = 'ajaybullex@gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False


class ConfigRemote:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://sql4413041:RVFWWnezJg@sql4.freemysqlhosting.net/sql4413041'
    SECRET_KEY = 'mintjtnrtjnbjt'
    SECURITY_REGISTERABLE = True
    SECURITY_PASSWORD_SALT = 'jnbtrbggtrnhguhtr'
    SECURITY_SEND_REGISTER_EMAIL = True
    SECURITY_SEND_EMAIL = True
    SECURITY_EMAIL_SENDER = 'ajaybullec@gmail.com'
    SECURITY_CONFIRMABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_POST_LOGIN_VIEW = ('author.admin')
    SECURITY_POST_LOGOUT_VIEW = ('security.login')
    SECURITY_POST_REGISTER_VIEW = '/login'
    SECURITY_POST_CONFIRM_VIEW = '/login'
    SECURITY_EMAIL_PLAINTEXT = False
    SECURITY_EMAIL_HTML = True
    SECURITY_FLASH_MESSAGES = True
    DISCUSSION_DISQUS_SHORTNAME = 'maxmuhanda'
    SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED = (
        'This Email is Registered to another account', 'error')
    SECURITY_MSG_USER_DOES_NOT_EXIST = ('This User Does not Exist!', 'error')
    SECURITY_DEFAULT_REMEMBER_ME = True
    UPLOADED_PHOTOS_DEST = STATIC_ROOT
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=2)

    DEBUG = False

    # flask ckeditor
    CKEDITOR_HEIGHT = 500
    CKEDITOR_WIDTH = 900
    CKEDITOR_ENABLE_CODESNIPPET = True
    CKEDITOR_CODE_THEME = 'atelier-dune.dark'

    # mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = 'ajaybullec@gmail.com'
    MAIL_PASSWORD = 'tlulkqxzyedrkvus'
    MAIL_DEFAULT_SENDER = 'ajaybullexgmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
