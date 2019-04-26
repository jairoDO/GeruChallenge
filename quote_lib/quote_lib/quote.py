"""
functions:

- get_quotes
- get_quote
"""
import os
try:
    from urllib.parse import urljoin
except ImportError as error:
    from urlparse import urljoin

import requests
import logging

URL_API_REST_DEFAULT = 'https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes/'
URL_API_REST = os.getenv('QUOTE_URL_API_REST', URL_API_REST_DEFAULT)

class NoDigitException(Exception):
    pass

class QuoteNotFound(Exception):
    pass

def get_quotes():
    """
    queries the API and returns a python dictionary containing all quotes available

    >>> response = get_quotes()
    >>> isinstance(response, dict)
    True
    >>> 'quotes' in response
    True
    >>> len(response .get('quotes')) > 0
    True


    :return: Json | None
    """
    return _request_to_json(URL_API_REST)
    return result


def get_quote(quote):
    """
    queries the API and returns a python dictionary containing the corresponding quote

    :param quote:
    :return: Json | Exception

    >>> result = get_quote(3)
    >>> isinstance(result, dict)
    True
    >>> 'quote'in result
    True
    >>> isinstance(result['quote'], str)
    True
    >>> result = get_quote('r')
    Traceback (most recent call last):
        ...
    quote.NoDigitException: The quote should be a digit
    >>> result = get_quote('1000000')
    Traceback (most recent call last):
        ...
    quote.QuoteNotFound: The number of quote no found

    """

    quote = str(quote)
    if not quote.isdigit():
        raise NoDigitException('The quote should be a digit')
    url = urljoin(URL_API_REST, quote)

    result = _request_to_json(url)
    if 'error' in result:
        if result['error'] == 'Not Found':
            raise QuoteNotFound('The number of quote no found')
        else:
            raise Exception(result['error'])
    return result

def _request_to_json(url):
    try:
        response = requests.get(url=url)
        result = response.json()
    except Exception as exception:
        logging.exception(exception)
        result = None
    return result
