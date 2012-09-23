from .. import utils, Base
from sqlalchemy import Column, ForeignKey, event
from sqlalchemy.types import String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship, backref

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer(), primary_key = True)
    given_name = Column(String(255))
    family_name = Column(String(255))
    suffix = Column(String(255))
    gender = Column(String(1))
    birthday = Column(DateTime())
    #birth_place
    deathday = Column(DateTime())
    #death_place
    father_id = Column(Integer, ForeignKey('people.id'))
    mother_id = Column(Integer, ForeignKey('people.id'))
    father = relationship("Person", 
                          remote_side = [id],
                          primaryjoin = "(Person.father_id == Person.id)",
                          )
    mother = relationship("Person", 
                          remote_side = [id],
                          primaryjoin = "(Person.mother_id == Person.id)",
                          )
    children = relationship("Person",
                             remote_side = [mother_id, father_id],
                             primaryjoin = "or_(Person.id == Person.mother_id, " \
                                          +"Person.id == Person.father_id)"
                           )
