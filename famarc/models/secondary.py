#Secondary tables
from . import Base
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.types import Integer

people_addresses = Table("people_addresses", Base.metadata,
    Column("person_id", Integer(), ForeignKey("people.id"), index=True),
    Column("place_id", Integer(), ForeignKey("places.id"), index=True),
)

people_phones = Table("people_phones", Base.metadata,
    Column("person_id", Integer(), ForeignKey("people.id"), index=True),
    Column("phone_id", Integer(), ForeignKey("phones.id"), index=True),
)

people_emails = Table("people_emails", Base.metadata,
    Column("person_id", Integer(), ForeignKey("people.id"), index=True),
    Column("email_id", Integer(), ForeignKey("emails.id"), index=True),
)

people_files = Table('people_files', Base.metadata,
    Column('person_id', Integer(), ForeignKey('people.id'), index=True),
    Column('file_id', Integer(), ForeignKey('files.id'), index=True),
)

people_places = Table('people_places', Base.metadata,
    Column('person_id', Integer(), ForeignKey('people.id'), index=True),
    Column('place_id', Integer(), ForeignKey('places.id'), index=True),
)

people_tags = Table('people_tags', Base.metadata,
    Column('person_id', Integer(), ForeignKey('people.id'), index=True),
    Column('tag_id', Integer(), ForeignKey('tags.id'), index=True),
)

tags_files = Table('tags_files', Base.metadata,
    Column('tag_id', Integer(), ForeignKey('tags.id'), index=True),
    Column('file_id', Integer(), ForeignKey('files.id'), index=True),
)

tags_places = Table('tags_places', Base.metadata,
    Column('tag_id', Integer(), ForeignKey('tags.id'), index=True),
    Column('place_id', Integer(), ForeignKey('places.id'), index=True),
)
