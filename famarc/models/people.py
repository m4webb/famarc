from .. import Base
from sqlalchemy import Column, ForeignKey, event, Table
from sqlalchemy.types import String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship, backref

people_addresses = Table("people_addresses", Base.metadata,
    Column("person_id", Integer(), ForeignKey("people.id")),
    Column("place_id", Integer(), ForeignKey("places.id")),
)

people_phones = Table("people_phones", Base.metadata,
    Column("person_id", Integer(), ForeignKey("people.id")),
    Column("phone_id", Integer(), ForeignKey("phones.id")),
)

people_emails = Table("people_emails", Base.metadata,
    Column("person_id", Integer(), ForeignKey("people.id")),
    Column("email_id", Integer(), ForeignKey("emails.id")),
)

class Person(Base):
    __tablename__ = "people"
    id = Column(Integer(), primary_key = True)
    given_name = Column(String(255))
    family_name = Column(String(255))
    suffix = Column(String(255))
    gender = Column(String(1))

    birthday = Column(DateTime())
    birthplace_id = Column(Integer(), ForeignKey("places.id"))
    birthplace = relationship("Place",
                   primaryjoin = "(Person.birthplace_id == Place.id)",
                   )

    deathday = Column(DateTime())
    deathplace_id = Column(Integer(), ForeignKey("places.id"))
    deathplace = relationship("Place",
                   primaryjoin = "(Person.deathplace_id == Place.id)",
                   )

    father_id = Column(Integer(), ForeignKey("people.id"))
    father = relationship("Person", 
               remote_side = [id],
               primaryjoin = "(Person.father_id == Person.id)",
               )
    
    mother_id = Column(Integer(), ForeignKey("people.id"))
    mother = relationship("Person", 
               remote_side = [id],
               primaryjoin = "(Person.mother_id == Person.id)",
               )

    children = relationship("Person",
                 remote_side = [mother_id, father_id],
                 primaryjoin = "or_(Person.id == Person.mother_id, " \
                              +"Person.id == Person.father_id)",
                 )

    addresses = relationship("Place", secondary = people_addresses)

    phones = relationship("Phone", secondary = people_phones)

    emails = relationship("Email", secondary = people_emails)

class Marriage(Base):
    __tablename__ = "marriages"
    id = Column(Integer(), primary_key = True)
    person1_id =  Column(Integer(), ForeignKey("people.id"))
    person1 = relationship("Person",
                primaryjoin = "(Person.id == Marriage.person1_id)",
                )
    person2_id =  Column(Integer(), ForeignKey("people.id"))
    person2 = relationship("Person",
                primaryjoin = "(Person.id == Marriage.person2_id)",
                )
    place_id = Column(Integer(), ForeignKey("places.id"))
    place = relationship("Place")
    begun = Column(DateTime())
    ended = Column(DateTime())
