from . import Base
from secondary import *
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import String, Integer
from sqlalchemy.orm import relationship, backref

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(2047))

    def __repr__(self):
        return '<Tag({})>'.format(self.name[:16])
