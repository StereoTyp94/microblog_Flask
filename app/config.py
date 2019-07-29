import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = 'Pavel Belov was born now'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mail.for.flask@gmail.com'
    MAIL_PASSWORD = 'CROCisFOREVER'
    ADMINS = ['alvin325@mail.ru']

    LANGUAGES = ['en', 'es']
'''
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
ADMINS = 'alvin325@mail.ru'

set MAIL_SERVER=smtp.gmail.com

from flask_mail import Message
from app import mail
msg = Message('test subject', sender=app.config['MAIL_USERNAME'], recipients=['alvin325@mail.ru'])
msg.body = 'text body'
msg.html = '<h1>HTML body</h1>'
mail.send(msg)

import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('justkiddingboat@gmail.com','just123kidding')
smtpObj.sendmail("justkiddingboat@gmail.com","michael.byrne@vice.com","go to bed!")
smtpObj.quit()
'''
