from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)


from app import routes, models

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    #return 'es'
