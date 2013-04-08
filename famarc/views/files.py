from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest

from ..models import (
    DBSession,
    files,
    tags,
    )
from .. import (
    utils,
    upload,
)

from ..exceptions import FamarcBaseException

import mimetypes

#------------------------------------------------------------------------------#

@view_config(
    context=files.File,
    name="", 
    renderer="famarc:templates/file_base.mak",
)
def file_base(request):
    return {"file" : request.context}

#------------------------------------------------------------------------------#

@view_config(
    context=files.File,
    name="view"
)
def file_view(request):
    file_obj = request.context
    response = Response(body=file_obj.read(),
                        content_type=mimetypes.types_map['.{}'.format(file_obj.ext.lower())],
                       )
    response.headerlist.append(('Content-Disposition', "filename={}.{}".format(
                                file_obj.name, file_obj.ext)))
    return response

#------------------------------------------------------------------------------#

@view_config(
    context=files.File,
    name="download"
)
def file_download(request):
    file_obj = request.context 
    response = Response(body=file_obj.read(),
                        content_type='application/force-download',
                       )
    response.headerlist.append(('Content-Disposition', "filename={}.{}".format(
                                file_obj.name, file_obj.ext)))
    return response

#------------------------------------------------------------------------------#

@view_config(
    context=files.File,
    name="tags.json",
    renderer="json",
)
def file_tags_json(request):
    return { "tags" : [[t.name] for t in request.context.tags]}

#------------------------------------------------------------------------------#

"""
@view_config(
    route_name='file_write',
)
def file_write(request):
    upload.upload_file(request.POST['file'].filename,
                       request.POST['file'].file,
                       file_desc = request.POST['description'])
    return Response('OK')

@view_config(
    route_name='file_addtag',
)
def file_addtag(request):
    file_id = request.matchdict['id']
    tag_name = request.POST['tag']
    upload.addtag(file_id, tag_name)
    return Response('OK')

@view_config(
    renderer="json",
    name="file_table.json",
)
def file_table_json(request):
    file_list = DBSession().query(files.File).all()
    return { "aaData" : [[f.id, f.name, f.ext, utils.datef(f.added), f.description] for f in
                          file_list]}



"""
