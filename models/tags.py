from .. import Base
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship, backref

tags_files = Table('tags_files', Base.metadata,
    Column('tag_id', Integer(), ForeignKey('tags.id')),
    Column('file_id', Integer(), ForeignKey('files.id'))
)

class Tag(Base):
    __tablename__ = 'tags' 
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    files = relationship("File", secondary = tags_files, backref="tags")

    def __init__(self, name):
        self.name = name 

    def __repr__(self):
        return '<Tag({})>'.format(self.name[:16])
