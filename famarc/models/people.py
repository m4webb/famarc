from . import Base
from secondary import *
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.orm import relationship

class Person(Base):
    __tablename__ = "people"
    id = Column(Integer(), primary_key = True)
    given_name = Column(String(255))
    family_name = Column(String(255))
    maiden_name = Column(String(255))
    suffix = Column(String(255))
    gender = Column(String(1))

    birthday = Column(DateTime())
    birthplace_id = Column(Integer(), ForeignKey("places.id"), index=True)
    birthplace = relationship("Place",
                   primaryjoin = "(Person.birthplace_id == Place.id)",
                   uselist = False,
                   )

    deathday = Column(DateTime())
    deathplace_id = Column(Integer(), ForeignKey("places.id"), index=True)
    deathplace = relationship("Place",
                   primaryjoin = "(Person.deathplace_id == Place.id)",
                   uselist = False,
                   )

    father_id = Column(Integer(), ForeignKey("people.id"), index=True)
    father = relationship("Person", 
               remote_side = [id],
               primaryjoin = "(Person.father_id == Person.id)",
               uselist = False,
               )
    
    mother_id = Column(Integer(), ForeignKey("people.id"), index=True)
    mother = relationship("Person", 
               remote_side = [id],
               primaryjoin = "(Person.mother_id == Person.id)",
               uselist = False,
               )

    children = relationship("Person",
                 remote_side = [mother_id, father_id],
                 primaryjoin = "or_(Person.id == Person.mother_id, " \
                              +"Person.id == Person.father_id)",
                 )

    """
    marriages = relationship("Marriage",
                 remote_side = [id],
                 primaryjoin = "or_(Person.id == Marriage.person1_id, " \
                              +"Person.id == Marriage.person2_id)",
                 )
    """

    addresses = relationship("Place", secondary = people_addresses,
                             backref="people")
    emails = relationship("Email", secondary = people_emails, backref="people")
    files = relationship("File", secondary = people_files, backref="people")
    phones = relationship("Phone", secondary = people_phones, backref="people")
    places = relationship("Place", secondary = people_places, backref="people")
    tags = relationship("Tag", secondary = people_tags, backref="people")

class Marriage(Base):
    __tablename__ = "marriages"
    id = Column(Integer(), primary_key = True)
    person1_id =  Column(Integer(), ForeignKey("people.id"), index=True)
    person1 = relationship("Person",
                primaryjoin = "(Person.id == Marriage.person1_id)",
                uselist = False,
                backref = "marriages"
                )
    person2_id =  Column(Integer(), ForeignKey("people.id"), index=True)
    person2 = relationship("Person",
                primaryjoin = "(Person.id == Marriage.person2_id)",
                uselist = False,
                backref = "marriages"
                )
    place_id = Column(Integer(), ForeignKey("places.id"), index=True)
    place = relationship("Place")
    begun = Column(DateTime())
    ended = Column(DateTime())
