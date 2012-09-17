settings = {

    'file_dir'  : '/Users/matthew/pylib/dbfiles/files',
    'db_file'   : '/Users/matthew/pylib/dbfiles/db/data.fs',
}

from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
storage = FileStorage(settings['db_file'])
db = DB(storage)
connection = db.open()
root = connection.root()
import transaction
import utils
import models
import upload
