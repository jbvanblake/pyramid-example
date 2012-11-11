from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    Route,
    Stop,
    )

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one':one, 'project':'app'}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_app_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
@view_config(route_name='route', renderer='templates/route.pt')
def route_view(request):
    return {'route_number': request.matchdict['route_number']}

@view_config(route_name='bus', renderer='templates/bus.pt')
def bus_view(request):
    return {'route_number': request.matchdict['route_number'],
            'bus_number': request.matchdict['bus_number']}

@view_config(route_name='stop', renderer='templates/stop.pt')
def stop_view(request):
    route_number = request.matchdict['route_number']
    new_route = Route(route_number)
    DBSession.add(new_route)

    stop_number = request.matchdict['stop_number']
    new_stop = Stop(stop_number)
    DBSession.add(new_stop)
    return {'route_number': request.matchdict['route_number'],
            'bus_number': request.matchdict['bus_number'],
            'stop_number': request.matchdict['stop_number']}
