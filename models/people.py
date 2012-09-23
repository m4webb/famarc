from .. import Base
from sqlalchemy import Column, ForeignKey, event
from sqlalchemy.types import String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship, backref

people_addresses = Table("people_addresses", Base.metadata,
    Column("person_id", Integer(), ForeignKey("people.id"))
    Column("place_id", Integer(), ForeignKey("places.id")),
)

people_phones = Table("people_phones", Base.metadata,
    Column("person_id", Integer(), ForeignKey("people.id"))
    Column("phone_id", Integer(), ForeignKey("phones.id")),
)

people_emails = Table("people_emails", Base.metadata,
    Column("person_id", Integer(), ForeignKey("people.id"))
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
                   primaryjoin = "(people.birthplace_id == places.id)",
                   )

    deathday = Column(DateTime())
    deathplace_id = Column(Integer(), ForeignKey("places.id"))
    deathplace = relationship("Place",
                   primaryjoin = "(people.deathplace_id == places.id)",
                   )

    father_id = Column(Integer, ForeignKey('people.id'))
    father = relationship("Person", 
               remote_side = [id],
               primaryjoin = "(Person.father_id == Person.id)",
               )
    
    mother_id = Column(Integer, ForeignKey('people.id'))
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
