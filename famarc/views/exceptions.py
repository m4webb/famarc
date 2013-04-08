from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest

from ..exceptions import FamarcBaseException

#------------------------------------------------------------------------------#

@view_config(
    context=FamarcBaseException
)
def FamarcBaseException_base(exception, request):
    return HTTPBadRequest(str(exception))

#------------------------------------------------------------------------------#
