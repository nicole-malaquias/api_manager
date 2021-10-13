import json

import requests
import sqlalchemy
import psycopg2
from app.configs.database import db
from app.exc.PackegeErrors import InvalidPackageError
from app.model.packege_release_model import PackageRelease
from app.model.project_model import Project
from flask import jsonify, request


def add_project():
 
    from flask import request 
    
    data = request.json
      
    try :
        
        project = Project(name = data['name'])
        
        db.session.add(project)
        db.session.commit()
        
        
        for tech in data['packages']:
            
            name_tech = tech['name']
                        
            request = requests.get(f'https://pypi.org/pypi/{name_tech}/json')
           
            response = json.loads(request.content)
            
            if not 'version' in tech :
                   
                version = response['info']['version'] 
            
                package = PackageRelease(name = name_tech, version = version, project_id = project.id)
                
                db.session.add(package)
                db.session.commit()
                
                return {"name": project.name,"packages":project.package_releases },201
            
            if not  tech['version'] in response['releases']:
                
                raise  InvalidPackageError
            
            package = PackageRelease(name = tech['name'], version = tech['version'], project_id = project.id)
            
            db.session.add(package)
            db.session.commit()
            
        return jsonify(data)
    
    
    except (InvalidPackageError,json.decoder.JSONDecodeError ) : 
       return {"Message": "One or more packages doesn't exist"},402
    
    except sqlalchemy.exc.IntegrityError as e :
        
        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'Message': str(e.orig).split('\n')[0]}, 400
        
        if type(e.orig) ==  psycopg2.errors.UniqueViolation:
            return {'Message': str(e.orig).split('\n')[0]}, 402    

def show_project_detail(project_name):
   
  
    query = Project.query.filter( Project.name == project_name ).all()
    
    return jsonify(query)

def delete_project(project_name):
    
    query = Project.query.filter( Project.name == project_name ).all()[0]
    if query is None:
         return {"Message":"Project not found!"},404
     
     
    db.session.delete(query)
    db.session.commit()
    return "",204

# @app.teardown_appcontext
def shutdown_session(exception=None):
    
    return ''
