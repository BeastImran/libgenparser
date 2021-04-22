import requests

from required_data import *


def get_page(query, title=False, year=False, isbn=False, md5=False, publisher=False,
             author=False, language=False, tag=False, extension=False) -> requests:
    """
    Uses respective url and returns the received requests object.

    :return: returns a respective requests object on success.
    """
    query_parsed = "+".join(query.split(" "))
    if title:
        return requests.get(BOOK_TITLE_SEARCH_URL.format(query_parsed))
    elif year:
        return requests.get(BOOK_YEAR_SEARCH_URL.format(query_parsed))
    elif isbn:
        return requests.get(BOOK_ISBN_SEARCH_URL.format(query_parsed))
    elif md5:
        return requests.get(BOOK_MD5_SEARCH_URL.format(query_parsed))
    elif publisher:
        return requests.get(BOOK_PUBLISHER_SEARCH_URL.format(query_parsed))
    elif author:
        return requests.get(BOOK_AUTHOR_SEARCH_URL.format(query_parsed))
    elif language:
        return requests.get(BOOK_LANGUAGE_SEARCH_URL.format(query_parsed))
    elif tag:
        return requests.get(BOOK_TAG_SEARCH_URL.format(query_parsed))
    elif extension:
        return requests.get(BOOK_EXTENSION_SEARCH_URL.format(query_parsed))
    else:
        return requests.get(BOOK_TITLE_SEARCH_URL.format(query_parsed))
