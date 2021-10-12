from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

@dataclass
class Project(db.Model):
    
    id: int 
    name: str
    package_releases: str
    
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    package_releases = relationship('PackageRelease',backref='project',cascade="all, delete-orphan")

    