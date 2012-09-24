from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scpoed_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

Base = declarative_base()
DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

import contacts
import places
import people
import files
import tags
