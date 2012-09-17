import os
import shutil
import hashlib 
from . import utils
from .models.files import File
from . import root
from . import transaction

def upload_file(file_path):
    """
    Upload the file located at the given path; insert a corresponding File
    object into root['files']; return the newly created File object.
    """
    file_sha1 = utils.sha1_from_path(file_path)
    if utils.sha1_exists(file_sha1):
        raise ValueError('file already in file directory')
    file_spath = utils.sha1_to_spath(file_sha1)
    file_dir = os.path.split(file_spath)[0]
    transaction.begin()
    #try:
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    shutil.copy(file_path, file_spath)
    file_object = File(file_sha1)
    root['files'][file_sha1] = file_object
    transaction.commit()
    return file_object
    '''
    except:
        if os.path.exists(file_spath):
            os.remove(file_spath)
            os.removedirs(file_spath)
        transaction.abort()
        return None
    '''
        
def upload_files(file_paths):
    res = []
    for file_path in file_paths:
        res.append(upload_file(file_path))
    return res

#if __name__==__main__:

