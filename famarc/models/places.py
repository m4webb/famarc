from . import Base
from secondary import *
from sqlalchemy import Column
from sqlalchemy.types import String, Integer, Float
from sqlalchemy.orm import relationship

class Place(Base):
    __tablename__ = 'places'
    id = Column(Integer(), primary_key = True)
    name = Column(String(255))
    street = Column(String(255))
    city = Column(String(255))
    state = Column(String(2))
    zip = Column(String(10))
    country = Column(String(2))
    longitutde = Column(Float())
    latitude = Column(Float())
    tags = relationship("Tag", secondary = tags_places, backref="places")

    def __repr__(self):
        return "<Place({})>".format(id)
