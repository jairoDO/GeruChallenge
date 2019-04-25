from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from datetime import datetime

from .models import SessionModel


from pyramid.events import subscriber
from pyramid.events import BeforeRender

@subscriber(BeforeRender)
def add_global(event):
    request = event['request']
    if request.path_info == '/sessions/requests':
        return
    if request.session.new:
        token = request.session.new_csrf_token()
        request.session['token'] = token
    else:
        token = request.session.get('token')
        if not token:
            token = request.session.new_csrf_token()
            request.session['token'] = token
    request.dbsession.add(
        SessionModel(
            identifier=token,
            datetime=datetime.now(),
            page=request.path_info

        )
    )



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')
    # config.add_tween('quotes.values_tween_factory')
    config.scan()
    my_session_factory = SignedCookieSessionFactory('itsaseekreet')
    config.set_session_factory(my_session_factory)
    return config.make_wsgi_app()


