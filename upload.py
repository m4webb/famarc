import os
import shutil
import hashlib 
from . import utils
from .models.files import File
from . import Session

def upload_file(file_path):
    """
    Upload the file located at the given path; insert a corresponding File
    object into root['files']; return the newly created File object.
    """
    session = Session()
    file_sha1 = utils.sha1_from_path(file_path)
    if utils.sha1_exists(file_sha1):
        raise ValueError('file already in file directory')
    file_spath = utils.sha1_to_spath(file_sha1)
    file_dir = os.path.split(file_spath)[0]
    session.begin()
    try:
        raise ValueError('This is my error')
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        shutil.copy(file_path, file_spath)
        file_object = File(file_sha1)
        session.add(file_object)
        session.commit()
        return file_object
    except:
        session.rollback()
        if os.path.exists(file_spath):
            os.remove(file_spath)
        if not os.listdir(file_dir):
            os.removedir(file_dir)
        raise
        
def upload_files(file_paths):
    res = []
    for file_path in file_paths:
        res.append(upload_file(file_path))
    return res

#if __name__==__main__:

