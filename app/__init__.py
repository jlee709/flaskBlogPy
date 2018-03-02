# creates application object as an instance of Flask Class
from flask import Flask

app = Flask(__name__)

from app import routes