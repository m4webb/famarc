import os
import shutil
import hashlib 
from . import utils
from .models.files import File
from . import Session

def upload_file(file_path):
    """
    Upload the file located at the given path; insert a corresponding File
    object into the database; return the newly created File object.
    """
    session = Session()
    file_name_ext = os.path.split(file_path)[1]
    file_tokens = file_name_ext.split('.')
    file_name = '.'.join(file_tokens[:-1])
    file_ext = file_tokens[-1]
    file_sha1 = utils.sha1_from_path(file_path)
    if utils.sha1_exists(file_sha1):
        raise ValueError('file already in file directory')
    file_spath = utils.sha1_to_spath(file_sha1)
    file_dir = os.path.split(file_spath)[0]
    try:
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        shutil.copy(file_path, file_spath)
        file_object = File(file_sha1)
        file_object.name = file_name
        file_object.ext = file_ext
        session.add(file_object)
        session.commit()
        return file_object.sha1
    except:
        session.rollback()
        if os.path.exists(file_spath):
            os.remove(file_spath)
        if os.path.exists(file_dir) and not os.listdir(file_dir):
            os.rmdir(file_dir)
        raise
        
def upload_files(file_paths):
    res = []
    for file_path in file_paths:
        res.append(upload_file(file_path, **kwargs))
    return res
