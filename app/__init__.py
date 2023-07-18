'''
In Python, a sub-directory that includes a __init__.py file is considered a package, and can be imported.
'''

'''
The __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used
'''

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes