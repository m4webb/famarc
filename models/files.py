import os
import hashlib
from persistent import Persistent
from .. import utils

class FileError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class File(Persistent):
    def __init__(self, sha1):
        self.sha1 = sha1
        if not os.path.isfile(utils.sha1_to_spath(self.sha1)):
            raise FileError('{}... does not map to existent file'.format(
                            sha1[:6]))

    def __repr__(self):
        return '<File({}...)>'.format(self.sha1[:6])

    def symlink(self, path):
        """
        Create a symbolic link to this file at <path>.
        """
        os.symlink(utils.sha1_to_spath(self.sha1), path)
