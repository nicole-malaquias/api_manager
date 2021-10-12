from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import backref, relationship 
from sqlalchemy import Column,Integer,String,ForeignKey

@dataclass
class PackageRelease(db.Model):
    
  
    name : str  
    version : int 
 
    
    __tablename__ = 'package_release'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(String)

    project_id = Column(Integer, ForeignKey('project.id'))

    def __init__(self, id=None, name=None, version=None, project_id=None):
        self.id = id
        self.name = name
        self.version = version
        self.project_id = project_id

   