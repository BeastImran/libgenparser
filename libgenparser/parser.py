import typing
from functools import lru_cache

import requests
from bs4 import BeautifulSoup

from .required_data import *


class LibgenParser:
    cache_length = 1000

    def __init__(self, custom_cache_length=1000):
        if custom_cache_length >= 0 and custom_cache_length != 1000:
            LibgenParser.cache_length = custom_cache_length

    @staticmethod
    @lru_cache(maxsize=cache_length)
    def __get_page(query, title=False, year=False, isbn=False, md5=False, publisher=False,
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

    @staticmethod
    def __parse_data(all_tables) -> list:
        """
        this method will parse the received HTML site.
        data will be parsed using table and their index positions
        as the positions of data in static through out the site.

        :param all_tables: received HTML file.
        :return: returns a list of dict on success.
        """
        data = []

        for table in all_tables:
            trs = table.find_all('tr')
            if len(trs) > 1:
                thumb = 'http://libgen.rs' + trs[1].find('img')['src']

                a = trs[1].find_all('a')
                book_url = 'http://libgen.rs' + a[0]['href']
                md5 = book_url.split('=')[-1]
                title = a[1].string
                del a

                author = trs[2].find('a').string
                year = trs[5].find_all('td')[1].string

                lang_and_pages = trs[6].find_all('td')
                lang = lang_and_pages[1].string
                pages = lang_and_pages[3].string
                del lang_and_pages

                book_id = trs[7].find_all('td')[3].string

                size_and_ext = trs[9].find_all('td')
                size = size_and_ext[1].string
                ext = size_and_ext[3].string
                del size_and_ext

                book = dict(zip(column_names,
                                [thumb, book_url, md5, title, author, year, lang, pages, book_id, size, ext]))

                data.append(book)

        return data

    def __send_to_parse(self, main_tables) -> typing.Union[list, None]:
        """
        Send received tables data to parsing stage if the required data table is available
        and returns the parsed list of dictionaries else returns None.

        :param main_tables:
        :return:
        """
        if len(main_tables) > 2:
            data = self.__parse_data(main_tables[2].find_all('table'))
            return data

    @lru_cache(maxsize=cache_length)
    def __beautify(self, result: requests) -> typing.Union[list, None]:
        """
        Uses BeautifulSoup to find all tables in site by using the received request response.
        The response is a requests object (which contains the html content).

        :param result:
        :return:
        """
        main_tables = BeautifulSoup(result.text, "lxml").find_all("table")
        return self.__send_to_parse(main_tables)

    @staticmethod
    @lru_cache(maxsize=cache_length)
    def resolve_download_link(md5) -> str:
        """
        resolves the book's download link by using it's md5 identifier
        and parses the download page of book for available download links
        and returns the first download link found.

        :param md5: md5 hash identifier of that specific book.
        :return: returns download url string of book on success.
        """
        return BeautifulSoup(requests.get(f"http://library.lol/main/{md5}").text, "lxml").find('li').find('a')['href']

    def download(self, md5: str, path: str) -> None:
        """
        downloads book using it's md5 identifier. Uses resolve_download_link method
        to get the book's download link. Write the file to provided path.

        :param md5: md5 identifier of book.
        :param path: full path to the destination folder included with file name.
        :return: returns True on successful download and write of file else return False.
        """
        url = self.resolve_download_link(md5)
        with open(path, 'wb+') as book:
            content = requests.get(url)
            book.write(content.content)

    def search_title(self, title: str) -> typing.Union[list[dict], None]:
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param title: string of title.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(self.__get_page(query=title.lower(), title=True))

    def search_author(self, author_name: str) -> typing.Union[list, None]:
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param author_name: string of title.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(self.__get_page(query=author_name.lower(), author=True))

    def search_year(self, year: str) -> typing.Union[list, None]:
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param year: string of year.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(self.__get_page(query=year, year=True))

    def search_md5(self, md5: str) -> typing.Union[list, None]:
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param md5: string of md5 identifier.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(self.__get_page(query=md5.lower(), md5=True))

    def search_publisher(self, publisher: str) -> typing.Union[list, None]:
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param publisher: publisher name.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(self.__get_page(query=publisher.lower(), publisher=True))

    def search_isbn(self, isbn: str) -> typing.Union[list, None]:
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param isbn: ISBN id of book.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(self.__get_page(query=isbn.lower(), isbn=True))

    def search_extension(self, extension: str) -> typing.Union[list, None]:
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param extension: extension of book to search.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(self.__get_page(query=extension.lower(), extension=True))

    def search_tag(self, tag: str) -> typing.Union[list, None]:
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param tag: tag string to search.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(self.__get_page(query=tag.lower(), tag=True))

    def search_language(self, language: str) -> typing.Union[list, None]:
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param language: language string to search.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(self.__get_page(query=language.lower(), language=True))
