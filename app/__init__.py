from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('route','route/{route_number}')
    config.add_route('bus','route/{route_number}/bus/{bus_number}')
    config.add_route('stop','route/{route_number}/bus/{bus_number}/stop/{stop_number}')
    config.scan()
    return config.make_wsgi_app()


# if __name__ == '__main__':
#     # configuration settings
#     settings = {}
#     settings['reload_all'] = True
#     settings['debug_all'] = True
#     settings['mako.directories'] = os.path.join(here, 'templates')
#     settings['db'] = os.path.join(here, 'tasks.db')
#     # session factory
#     session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
#     # configuration setup
#     config = Configurator(settings=settings, session_factory=session_factory)
#     # routes setup
#     config.add_route('list', '/')
#     config.add_route('new', '/new')
#     config.add_route('close', '/close/{id}')
#     # static view setup
#     config.add_static_view('static', os.path.join(here, 'static'))
#     # scan for @view_config and @subscriber decorators
#     config.scan()
#     # serve app
#     app = config.make_wsgi_app()
#     server = make_server('0.0.0.0', 8080, app)
#     server.serve_forever()
# 
