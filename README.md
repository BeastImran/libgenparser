# LIBGEN-PARSER

Lets you parse libgen website easily. Uses [libgen.rs](http://libgen.rs) site.

### Quick LINKS
#
1. [Installation](#installation)

2. [Requirements](#requirements)

    * [Dependencies](#dependencies)

    * [Missing Module issues](#missing-modules)

3. [Usage](#usage)

4. [Supported Features](#supported-features)

### INSTALLATION
#

Use the below command to install and start using.

```bash
$ pip install libgenparser
```

### REQUIREMENTS
#

#### Dependencies

This package has following dependencies. All of them probably will be installed automatically.

* [requests](https://pypi.org/project/requests/)
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [lxml](https://pypi.org/project/lxml/) (for fast parsing of html)
* [async-cache](https://pypi.org/project/async-cache/) (only if you plan to use async methods) (optional)

#### Missing modules

If not installed automatically, use the below respective commands to install missing modules. Follow as bellow:

* All of them at once:

    ```bash
    $ pip install requests beautifulsoup4 lxml async-cache
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

    * Install `lxml` parser for html parsing by beautifulsoup4

      ```bash
      $ pip install lxml
      ```

    * Install `async-cache` only if you plan to use async version.

      ```bash
      $ pip install async-cache
      ```

### USAGE
#

Start using by importing as follows.

```python
from libgenparser.parser import LibgenParser

libgen = LibgenParser()
libgen.search_title("Clean python")
```

***LibgenParser*** class is contains all the required methods. All methods except `LibgenParser.resolve_download_link()`
returns parsed ***list of dictionaries*** on success else they return ***None***. All methods are cached using
***functools.lru_cache()*** for faster results. Async methods in `__future__` are cached using `async-cache`
module's `cache.AsyncLRU`.

By default, cache_length (amount of objects to hold in memory) is 1000. This might be an issue of out of memory if you
are running on very low memory machine. Change it as required by assigning a value (as length) to `custom_cache_length`
in LibgenParser class as shown bellow. Setting it to `0` will store no cache.

**Change cache length**

```python
from libgenparser.parser import LibgenParser

libgen = LibgenParser(custom_cache_length=100)
libgen.search_title("Clean python")
```

* Provide a title string to `libgen.search_title()`.


* Provide author's name string to`libgen.search_author()`.


* Provide year value (int/string) to `libgen.search_year()`.


* Provide MD5 identifier string of ebook to `libgen.search_md5()`.


* Provide publisher's name string to `libgen.search_publisher()`.


* Provide ISBN identifier string of ebook to `libgen.search_isbn()`.


* Provide file extension string of ebook to `libgen.searcg_extension()`.


* Provide language string to `libgen.search_language()`.


* Provide tag string to `libgen.search_tag()`.

<br>

**This package has asynchronous (asyncio) support also.**

```python
from libgenparser.__future__.parser import LibgenParser
```

`LibgenParser` from `__future__` package contains async versions of all methods.

### Supported features
#

* Download link

Get download links of an ebook on libgen.rs site by using its MD5 identifier.

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
