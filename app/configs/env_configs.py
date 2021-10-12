from dotenv import load_dotenv
from flask import Flask
from os import environ
import os 
load_dotenv()

def init_app(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = bool(environ.get('SQLALCHEMY_TRACK_MODIFIC'))
    
    app.config['JSON_SORT_KEYS'] = False

    if os.environ.get('FLASK_ENV') == 'production':
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql')
    else :
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')