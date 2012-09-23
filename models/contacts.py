from .. import Base
from sqlalchemy import Column
from sqlalchemy.types import String, Integer, Float
from places import Place

tags_files = Table('tags_files', Base.metadata,
    Column('tag_id', Integer(), ForeignKey('tags.id')),
    Column('file_id', Integer(), ForeignKey('files.id'))
)

class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer(), primary_key = True)
    name = Column(String(255))
    number = Column(String(255))

class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer(), primary_key = True)
    name = Column(String(255))
    address = Column(String(255))
