import os
#from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') # protect against CSRF attacks
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAILGUN_SMTP_SERVER', '')
    MAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT', '')
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAILGUN_SMTP_LOGIN', '')
    MAIL_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD', '')
    MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN', '')
    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY', '')
    DEFAULT_MAIL_SENDER = 'csprojects200220@gmail.com'
    ADMINS = ['jedhcl@gmail.com']
    POSTS_PER_PAGE = 3
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
