# All required search urls
BOOK_TITLE_SEARCH_URL = "http://libgen.rs/search.php?req={}&lg_topic=libgen&open=0&view=detailed&res=25&phrase=1&column=def"
BOOK_AUTHOR_SEARCH_URL = "http://libgen.rs/search.php?req={}&lg_topic=libgen&open=0&view=detailed&res=25&phrase=1&column=author"
BOOK_YEAR_SEARCH_URL = "http://libgen.rs/search.php?req={}&open=0&res=25&view=detailed&phrase=1&column=year"
BOOK_MD5_SEARCH_URL = "http://libgen.rs/search.php?req={}&open=0&res=25&view=detailed&phrase=1&column=md5"
BOOK_PUBLISHER_SEARCH_URL = "http://libgen.rs/search.php?req={}&open=0&res=25&view=detailed&phrase=1&column=publisher"
BOOK_ISBN_SEARCH_URL = "http://libgen.rs/search.php?req=1775093328&open=0&res=25&view=detailed&phrase=1&column=identifier"
BOOK_LANGUAGE_SEARCH_URL = "http://libgen.rs/search.php?req={}&open=0&res=25&view=detailed&phrase=1&column=language"
BOOK_TAG_SEARCH_URL = "http://libgen.rs/search.php?req={}&open=0&res=25&view=detailed&phrase=1&column=tags"
BOOK_EXTENSION_SEARCH_URL = "http://libgen.rs/search.php?req={}&open=0&res=25&view=detailed&phrase=1&column=extension"

# will be used to map data parsed on site.
col_names = [
    'Thumb',
    'Download_link',
    'MD5',
    'Title',
    'Author',
    'Year',
    'Language',
    'Pages',
    'ID',
    'Size',
    'Extension',
]
