# creates application object as an instance of Flask Class
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes