
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.configs import env_configs , database ,  migrations
from app.views import api_blueprint

def create_app():
    
    app  = Flask(__name__)
    env_configs.init_app(app)
    database.init_app(app)
    migrations.init_app(app)
    
    app.register_blueprint(api_blueprint.bp)
    
    return app
