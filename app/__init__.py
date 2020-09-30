from flask              import Flask, request
from flask_login        import LoginManager
from flask_sqlalchemy   import SQLAlchemy
from flask_migrate      import Migrate
from flask_babel        import Babel, lazy_gettext as _l
from flask_bootstrap    import Bootstrap
import  config


app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

Bootstrap(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login_adm'


babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

from app import routes, models 
