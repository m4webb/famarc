import os
from .. import utils
from . import Base
from secondary import *
from sqlalchemy import Column, event, ForeignKey, Table
from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.orm import relationship, backref

class FileError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class File(Base):
    __tablename__ = 'files' 
    id = Column(Integer(), primary_key = True)
    sha1 = Column(String(40), nullable = False, unique = True)
    name = Column(String(255))
    ext = Column(String(255))
    description = Column(String(2047))
    added = Column(DateTime())
    tags = relationship("Tag", secondary = tags_files, backref="files")

    def __init__(self, sha1):
        self.sha1 = sha1
        if not utils.sha1_exists(sha1):
            raise FileError('{}... does not map to existent file'.format(
                            sha1[:6]))

    def __repr__(self):
        return '<File({}...)>'.format(self.sha1[:6])

    def _json_(self):
        """
        Return an object psuedo-copy that can be json serialized. 
        
        This should be viewed as a read-only method, as there is (currently) no
        way to map changes back to the object.
        """
        return {
            'id'            : self.id,
            'sha1'          : self.sha1,
            'name'          : self.name,
            'ext'           : self.ext,
            'description'   : self.description,
            'added'         : utils.datef(self.added),
            'people'        : [person._json_() for person in self.people],
            'tags'          : [tag._json_() for tag in self.tags],
        }

    def read(self):
        return open(utils.sha1_to_spath(self.sha1)).read()

    def symlink(self, path):
        """
        Create a symbolic link to this file at <path>.
        """
        os.symlink(utils.sha1_to_spath(self.sha1), path)


def after_delete_listener(mapper, connection, target_file):
    file_spath = utils.sha1_to_spath(target_file.sha1)
    file_dir = os.path.split(file_spath)[0]
    if os.path.exists(file_spath):
        os.remove(file_spath)
    if os.path.exists(file_dir) and not os.listdir(file_dir):
        os.rmdir(file_dir)

event.listen(File, 'after_delete', after_delete_listener)
