from sqlalchemy.orm.exc import NoResultFound
from .models import DBSession, files, tags
from .exceptions import IdDoesNotExist, BadId

class ObjectLookup(object):

    def __getitem__(self, item):
        try:
            return DBSession.query(self.object_class).filter(
                                   self.object_class.id == int(item)
                                  ).one()
        except NoResultFound:
            raise IdDoesNotExist(self.object_class, item)
        except ValueError:
            raise BadId(item)

class FileLookup(object):
    pass



"""
root = {
    'files' : ObjectLookup(files.File),
    'tags'  : ObjectLookup(tags.Tag),
}
"""

root_factory = None
