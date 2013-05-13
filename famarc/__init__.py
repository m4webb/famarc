file_dir = "/Users/matthew/pylib/famarc/testdata/"

import models

from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

from traversal import root_factory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings, root_factory=root_factory)
    config.add_static_view('static', 'static', cache_max_age=3600)
    """
    config.add_route('file_upload', '/')
    config.add_route('file_write', '/file_write')   
    config.add_route('file_base', '/files/{id:\d+}')
    config.add_route('file_view', '/files/{id:\d+}/view')
    config.add_route('file_download', '/files/{id:\d+}/download')
    config.add_route('file_addtag', '/files/{id:\d+}/addtag')
    config.add_route('files_list', '/files')   
    config.add_route('tags_list', '/tags')   
    config.add_route('file_tags.json', '/files/{id:\d+}/file_tags.json')   
    """
    config.scan()
    return config.make_wsgi_app()
