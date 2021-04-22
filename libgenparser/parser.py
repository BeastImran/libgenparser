import typing

from bs4 import BeautifulSoup

from .pages import *


class LibgenParser:

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

                book = dict(zip(col_names,
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

    def __beautify(self, result: requests):
        """
        Uses BeautifulSoup to find all tables in site by using the received request response.
        The response is a requests object (which contains the html content).

        :param result:
        :return:
        """
        main_tables = BeautifulSoup(result.text, "lxml").find_all("table")
        return self.__send_to_parse(main_tables)

    @staticmethod
    def resolve_download_link(md5) -> str:
        """
        resolves the book's download link by using it's md5 identifier
        and parses the download page of book for available download links
        and returns the first download link found.

        :param md5: md5 hash identifier of that specific book.
        :return: returns download url string of book on success.
        """
        return BeautifulSoup(requests.get(f"http://library.lol/main/{md5}").text, "lxml").find('li').find('a')['href']

    def search_title(self, title: str) -> typing.Union[list, None]:
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param title: string of title.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(get_page(query=title, title=True))

    def search_author(self, author_name: str):
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param author_name: string of title.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(get_page(query=author_name, author=True))

    def search_year(self, year: typing.Union[str, int]):
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param year: string of year.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(get_page(query=year, year=True))

    def search_md5(self, md5: str):
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param md5: string of md5 identifier.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(get_page(query=md5, md5=True))

    def search_publisher(self, publisher: str):
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param publisher: publisher name.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(get_page(query=publisher, publisher=True))

    def search_isbn(self, isbn: str):
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param isbn: ISBN id of book.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(get_page(query=isbn, isbn=True))

    def search_extension(self, extension: str):
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param extension: extension of book to search.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(get_page(query=extension, extension=True))

    def search_tag(self, tag: str):
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param tag: tag string to search.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(get_page(query=tag, tag=True))

    def search_language(self, language: str):
        """
        requests site with title (string) and returns list of parsed dictionary data on success.

        :param language: language string to search.
        :return: list: list of parsed dictionary data on success.
        :return: None when search result was empty (most probably title not found (empty result))
        """
        return self.__beautify(get_page(query=language, language=True))
