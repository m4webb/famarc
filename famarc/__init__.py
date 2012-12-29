file_dir = '/Users/matthew/pylib/famarc/data/'

from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('file_upload', '/')
    config.add_route('file_write', '/file_write')   
    config.add_route('file_get', '/files/{id:\d+}')
    config.add_route('files', '/files')   
    config.scan()
    return config.make_wsgi_app()
