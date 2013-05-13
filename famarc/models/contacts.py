from . import Base
from sqlalchemy import Column
from sqlalchemy.types import String, Integer

class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer(), primary_key = True)
    name = Column(String(255))
    address = Column(String(255))

class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer(), primary_key = True)
    name = Column(String(255))
    number = Column(String(255))
