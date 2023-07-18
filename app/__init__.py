'''
In Python, a sub-directory that includes a __init__.py file is considered a package, and can be imported.
'''

'''
The __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used
'''

from flask import Flask
from flask_login import LoginManager
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


from app import routes, models