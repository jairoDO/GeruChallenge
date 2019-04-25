import random
from itertools import groupby
from operator import attrgetter

import transaction

from pyramid.view import view_config
from quote_lib.quote import get_quotes, get_quote, QuoteNotFound, NoDigitException
from ..models import SessionModel


@view_config(route_name='quotes', renderer='../templates/quotes.jinja2')
def quotes(request):
    quotes = get_quotes()
    return {'quotes': quotes['quotes']}


@view_config(route_name='get_quote', renderer='../templates/quote.jinja2')
def get_quote_view(request):
    id_quote = request.matchdict['id_quote']
    quote = {}
    try:
        quote = get_quote(id_quote)
    except QuoteNotFound:
        no_found = True
        error = True
    except NoDigitException:
        error = True
    return locals()


@view_config(route_name='random', renderer='../templates/random.jinja2')
def random_view(request):
    id_quote = random.choices(range(0, 19)).pop()
    quote = get_quote(id_quote)
    return locals()


@view_config(route_name='requests', renderer='json')
def requests(request):
    with transaction.manager:
        requests = request.dbsession.query(SessionModel).all()
        groupby_identifier = groupby(requests, key=attrgetter('identifier'))
        requests_dict = {identifier: list(map(SessionModel.to_json, row)) for identifier, row in groupby_identifier}

    return {'total_request': len(requests), 'total_sessions': len(requests_dict), 'requests': requests_dict}
