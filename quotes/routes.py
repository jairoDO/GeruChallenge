def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('quotes', '/quotes')
    config.add_route('random', '/quotes/random')
    config.add_route('get_quote', '/quotes/{id_quote}')
    config.add_route('requests', '/sessions/requests')
