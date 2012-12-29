from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from sqlalchemy.orm.exc import NoResultFound

from .models import (
    DBSession,
    files,
    )
from . import (
    utils,
    upload,
)

import mimetypes

@view_config(
   route_name='file_upload',
   renderer='famarc:templates/file_upload.mak',
)
def file_upload(request):
    return {}

@view_config(
    route_name='file_write',
)
def file_write(request):
    upload.upload_file(request.POST['file'].filename,
                       request.POST['file'].file,
                       file_desc = request.POST['description'])
    return Response('OK')

@view_config(
    route_name='files', 
    renderer='famarc:templates/files.mak',
)
def file_list(request):
    session = DBSession()
    return {'files':session.query(files.File).all()}

@view_config(
    renderer="json", 
    name="file_list.json",
)
def file_list_json(request):
    return [file._json_() for file in DBSession().query(files.File).all()]

@view_config(
    renderer="json",
    name="file_table.json",
)
def file_table_json(request):
    file_list = DBSession().query(files.File).all()
    return { "aaData" : [[f.id, f.name, f.ext, utils.datef(f.added), f.description] for f in
                          file_list]}


@view_config(
    route_name="file_get",
)
def file_get(request):
    try:
        file_obj = DBSession.query(files.File).filter(files.File.id ==
                                   int(request.matchdict['id'])).one()
        response = Response(body=open(utils.sha1_to_spath(file_obj.sha1)).read(),
                        content_type=mimetypes.types_map['.{}'.format(file_obj.ext.lower())],
                        )
        response.headerlist.append(('Content-Disposition', "filename={}.{}".format(
                                    file_obj.name, file_obj.ext)))
        return response
    except NoResultFound:
        return Response(body="No such file {}".format(
                        request.matchdict['id']), 
                        content_type="text/plain")

'''
@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one':one, 'project':'famarc'}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_famarc_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
'''
