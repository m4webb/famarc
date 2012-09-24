from . import Base
from sqlalchemy import Column
from sqlalchemy.types import String, Integer, Float

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
