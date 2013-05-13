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

from ..traversal import ObjectLookup

from ..exceptions import FamarcBaseException

from sqlalchemy import func

from sqlalchemy.sql.expression import or_

import mimetypes

#------------------------------------------------------------------------------#

@view_config(
    context=ObjectLookup, 
    name='', 
    renderer='famarc:templates/files.mak',
)
def files_list(request):
    return {}

#------------------------------------------------------------------------------#

@view_config(
    context=ObjectLookup, 
    name="data.json",
    renderer="json",
)
def file_data(request):

    #Count all records
    json_response = {}
    json_response["iTotalRecords"] = DBSession.query(func.count(files.File.id)
                                                    ).one()[0]

    #Filter
    query = DBSession.query(files.File)
    query = query.filter(or_(
        files.File.name.like("%{}%".format(request.POST['sSearch'])),
        files.File.description.like("%{}%".format(request.POST['sSearch'])),
        files.File.ext.like("%{}%".format(request.POST['sSearch'])),
    ))

    #Count filtered records
    json_response["iTotalDisplayRecords"] = query.count()

    #Slice
    slice_start = int(request.POST['iDisplayStart'])
    slice_len = int(request.POST['iDisplayLength'])
    query = query.slice(slice_start, slice_start+slice_len)

    #Get data and finalize
    file_list = query.all()
    json_response["aaData"] = [[f.id, f.name, f.ext, utils.datef(f.added),
                                f.description] for f in file_list]
    json_response["sEcho"] = str(int(request.POST['sEcho']))

    return json_response

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
