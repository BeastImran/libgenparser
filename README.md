# LIBGEN-PARSER

Lets you parse libgen website easily. Uses libgen.rs site as domain.

-------------------------------------------------

### REQUIRMENTS

This package has following dependencies.

* requests
* beautifulsoup4
* lxml (for fast parsing of html)

should be installed automatically, if not follow as bellow.

* All of them at once:

    ```bash
    $ pip install requests beautifulsoup4 lxml
    ```

* Install individually

    * Install `requests`

    ```bash
    $ pip install requests
    ```

    * Install `beautifulsoup4`

    ```bash
    $ pip install beautifulsoup4
    ```

    * Install `lxml`

    ```bash
    $ pip install lxml
    ```

-------------------------------------------------

### INSTALATION

use the below command to install and start using.

```bash
$ pip install libgenparser
```

-------------------------------------------------

### USAGE

Start using by importing as follows.

```python
from libgenparser import parser
```

`parser` class is contains all the required methods. Create and object of it and start using its methods as required.
All methods except *parser.resolve_download_link()* returns *parsed list of dictionaries* on success else they return
*None*.

* Provide a string as title to `parser.search_title()`.


* Provide a string as author's name to`parser.search_author()`.


* Provide year value to `parser.search_year()`.


* Provide MD5 identifier string of ebook to  `parser.search_md5()`.


* Provide a string of publisher's name to `parser.search_publisher()`.


* Provide ISBN identifier string of ebook to `parser.search_isbn()`.


* Provide file extension string of ebook to `parser.searcg_extension()`.


* Provide language string to `parser.search_language()`.


* Provide tag string to `parser.search_tag()`.

<br>

**This package has asynchronous support also.**

```python
from libgenparser.__future__ import parser
```

`libgenparser.__future__.parser` contains async versions of all methods.

-------------------------------------------------

### Supported features

* Download link

Get download link of a specific book by passing the MD5 identifier of that book to `parser.resolve_download_link()`
which returns a direct url of book to download. MD5 identifiers can be obtained on use of search method.

Can query libgen.rs with following filters:

* Title (default)
* Tag
* Author name
* Year
* MD5
* ISBN
* Publisher
* Language
* File extension
