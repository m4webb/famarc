settings = {

    'file_dir'  : '/Users/matthew/pylib/dbfiles/files',
    'db_file'   : '/Users/matthew/pylib/dbfiles/db/data.db',
}

#sqlalchemy init
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///{}'.format(settings['db_file']))
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)

#package init
import utils
import models
import upload
