from flask import Flask 
from flask_migrate import Migrate  

def init_app(app: Flask):
    
    from app.model.project_model import Project
    from app.model.packege_release_model import PackageRelease
   
    Migrate(app, app.db)
    
