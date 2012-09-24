import os
import hashlib
from . import file_dir 

class Sha1Error(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def spath_to_sha1(spath):
    sha1 = ''.join(spath.split(os.sep)[-2:])
    if len(sha1) != 40:
        raise ValueError('Bad spath.')
    else:
        return sha1

def sha1_to_spath(sha1):
    if len(sha1) != 40:
        raise ValueError('Bad sha1 code.')
    else:
        return os.path.join(file_dir,sha1[:2],sha1[2:])

def sha1_exists(sha1):
    '''
    Return True if a file exists for sha1.
    '''
    return os.path.isfile(sha1_to_spath(sha1))

def sha1_check(sha1):
    '''
    Check the sha1 of the file at sha1_to_spath(sha1).

    A Sha1Error will be raised if the file does not exist, or if the sha1 sums
    do not match. 
    '''
    spath = sha1_to_spath(sha1)
    if not sha1_exists(sha1):
        raise Sha1Error('no file found for {}...'.format(sha1[:6]))
    if sha1 != sha1_from_path(sha1_to_spath(sha1)):
        raise Sha1Error('sha1 sums do not match for {}...'.format(sha1[:6]))

def sha1_from_path(path, block_size=1024):
    '''
    Return the hexdigest for the file located at path.
    '''
    sha1 = hashlib.sha1()
    with open(path) as f:
        for chunk in iter(lambda: f.read(block_size), b''): 
            sha1.update(chunk)
        return sha1.hexdigest()
