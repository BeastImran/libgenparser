# LIBGEN-PARSER

Lets you parse libgen website easily. Uses [libgen.rs](http://libgen.rs) site.

### Quick Links
#

1. [Installation](#installation)

2. [Requirements](#requirements)

    . [Dependencies](#dependencies)

    . [Missing Module issues](#missing-modules)

3. [Usage](#usage)

4. [Supported Features](#supported-features)

5. [Examples](#examples)

    . [Initial steps](#initial-steps-to-get-started)
    
    . [Search examples](#search-examples)

    . [Download examples](#download-stuff)

6. [Final words](#final-words)

### INSTALLATION

#

Use the below command to install and start using.

```bash
$ pip install libgenparser
```

### REQUIREMENTS
#

Project was built on [[c]python3](https://www.python.org/downloads/). Pip must be up-to-date.

To update pip, do as follows:

```bash
$ python -m pip install -U pip
```

#### Dependencies

This package has following dependencies. All of them probably will be installed automatically.

* [requests](https://pypi.org/project/requests/)
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [lxml](https://pypi.org/project/lxml/) (for fast parsing of html)
* [async-cache](https://pypi.org/project/async-cache/) (for caching of async methods) (optional)

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

***LibgenParser*** class is contains all the required methods. All methods except `LibgenParser.resolve_download_link()` returns parsed ***list of dictionaries*** on success else they return ***None***. All methods are cached using ***functools.lru_cache()*** for faster results. Async methods in `__future__` are cached using `async-cache` module's `cache.AsyncLRU`.

By default, cache_length (amount of objects to hold in memory) is 1000. This might be an issue of out of memory if you are running on very low memory machine. Change it as required by assigning a value (as length) to `custom_cache_length` in LibgenParser class as shown bellow. Setting it to `0` will store no cache.

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

* Provide MD5 identifier to `libgen.resolve_download_link()`

* Provide MD5 identifier and path to download file to `libgen.download()`


**This package has asynchronous (asyncio) support also.**

```python
from libgenparser.__future__.parser import LibgenParser
```

`LibgenParser` from `__future__` package contains async versions of all methods.

### Supported features

#

* **Download file using md5 identifier.**

    Download file using md5 identifier of that specific book by using `parser.download()` method. It takes two arguments, md5 string and path of file to store. See this example.


* **Generate download link.**

    Get direct download link of a specific book by passing the MD5 identifier of that book to `parser.resolve_download_link()` which returns a direct url of book to download. MD5 identifiers can be obtained on use of search method.


* **Search for following fields**

    Can query libgen.rs to search in following fields by using respective method shown above.


    * Title (default)
    * Tag
    * Author name
    * Year
    * MD5
    * ISBN
    * Publisher
    * Language
    * File extension


## Examples

### Initial steps to get started

For synchronous code:
```python3
from libgenparser.parser import LibgenParser
libgen = LibgenParser() # LibgenParser(custom_cache_length=<NUMBER>), NUMBER=0 no cache
```

For asynchronous code:
```python3
from libgenparser.__future__.parser import LibgenParser
libgen = LibgenParser() # LibgenParser(custom_cache_length=<NUMBER>), NUMBER=0 no cache
```

Any search result will be a list of dictionaries with following fields holding respective data. Some of these fields can be empty on site, which will be specified by `None` which means the data was not found for that specific book. Guaranteed fields are noted in comments. 

```python3
column_names = [
    'Thumb', # holds book's thumbnail url.
    'Download_link', # holds book's download site's link. Not to be confused with direct download. Guaranteed Field.
    'MD5', # holds unique MD5 identifier of book. Guaranteed Field.
    'Title', # the title of book. Guaranteed Field.
    'Author', # the author of book
    'Year', # the year of publish
    'Language', # language of book
    'Pages', # number of pages in book
    'ID', # id of book on libgen.rs site. Guaranteed Field.
    'Size', # size of book (kb, mb, KB, MB etc)
    'Extension', # the format of book (.pdf, .djvu, .epub, .chm etc)
]
```

### Search examples

To search a title:

```python3
search_result = libgen.search_title("Python")[:5]
```

<details>
<summary>output</summary>
{'Thumb': 'http://libgen.rs/covers/0/aee7239ffcf7871e1d6687ced1215e22-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=AEE7239FFCF7871E1D6687CED1215E22', 'MD5': 'AEE7239FFCF7871E1D6687CED1215E22', 'Title': 'Exploring Python', 'Author': 'Markus Nix', 'Year': '2005', 'Language': 'German', 'Pages': '174', 'ID': '801', 'Size': '2 Mb (1691080)', 'Extension': 'djvu'}

{'Thumb': 'http://libgen.rs/covers/1000/8b7f9439ff75aeac89b8748bdbc1e1d3-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=8B7F9439FF75AEAC89B8748BDBC1E1D3', 'MD5': '8B7F9439FF75AEAC89B8748BDBC1E1D3', 'Title': 'Beginning Python', 'Author': 'Peter C. Norton', 'Year': '2005', 'Language': 'English', 'Pages': '679', 'ID': '1464', 'Size': '4 Mb (3670658)', 'Extension': 'pdf'}

{'Thumb': 'http://libgen.rs/covers/1000/8288fdbd7e6d373accbc9d274ff42b29-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=8288FDBD7E6D373ACCBC9D274FF42B29', 'MD5': '8288FDBD7E6D373ACCBC9D274FF42B29', 'Title': 'Python essential reference', 'Author': 'David Beazley', 'Year': '2001', 'Language': 'English', 'Pages': '586', 'ID': '1473', 'Size': '4 Mb (4308155)', 'Extension': 'djvu'}

{'Thumb': 'http://libgen.rs/covers/1000/1834e0e4df316dc07956cff0c63bda92-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=1834E0E4DF316DC07956CFF0C63BDA92', 'MD5': '1834E0E4DF316DC07956CFF0C63BDA92', 'Title': 'Foundations of Python network programming', 'Author': 'John Goerzen', 'Year': '2004', 'Language': 'English', 'Pages': '538', 'ID': '1482', 'Size': '3 Mb (3024636)', 'Extension': 'djvu'}

{'Thumb': 'http://libgen.rs/covers/1000/31debc732ae60d265ba551a112fbe6bd-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=31DEBC732AE60D265BA551A112FBE6BD', 'MD5': '31DEBC732AE60D265BA551A112FBE6BD', 'Title': 'Making use of Python', 'Author': 'Rashi Gupta', 'Year': '2002', 'Language': 'English', 'Pages': '416', 'ID': '1486', 'Size': '3 Mb (3187656)', 'Extension': 'pdf'}

</details>

To search an author:

```python3
search_result = libgen.search_author("Markus Nix")[:5]
```

<details>
<summary>output</summary>
{'Thumb': 'http://libgen.rs/covers/0/aee7239ffcf7871e1d6687ced1215e22-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=AEE7239FFCF7871E1D6687CED1215E22', 'MD5': 'AEE7239FFCF7871E1D6687CED1215E22', 'Title': 'Exploring Python', 'Author': 'Markus Nix', 'Year': '2005', 'Language': 'German', 'Pages': '174', 'ID': '801', 'Size': '2 Mb (1691080)', 'Extension': 'djvu'}

{'Thumb': 'http://libgen.rs/covers/659000/8f35df56f73b2c9baddf88b57387450c-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=8F35DF56F73B2C9BADDF88B57387450C', 'MD5': '8F35DF56F73B2C9BADDF88B57387450C', 'Title': 'Exploring JavaScript. Von Insidern lernen  GERMAN ', 'Author': 'Markus Nix', 'Year': None, 'Language': 'German ', 'Pages': '166', 'ID': '659804', 'Size': '2 Mb (2390174)', 'Extension': 'pdf'}
</details>

To search using MD5 identifier:

```python3
search_result = libgen.search_md5("AEE7239FFCF7871E1D6687CED1215E22")
```

<details>
<summary>output</summary>
{'Thumb': 'http://libgen.rs/covers/0/aee7239ffcf7871e1d6687ced1215e22-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=AEE7239FFCF7871E1D6687CED1215E22', 'MD5': 'AEE7239FFCF7871E1D6687CED1215E22', 'Title': 'Exploring Python', 'Author': 'Markus Nix', 'Year': '2005', 'Language': 'German', 'Pages': '174', 'ID': '801', 'Size': '2 Mb (1691080)', 'Extension': 'djvu'}
</details>

To search using extension:

```python3
search_result = libgen.search_extension("chm")[-5:]
```

<details>
<summary>output</summary>
{'Thumb': 'http://libgen.rs/covers/0/4787b628578fa3dc2d29603e369348a8-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=4787B628578FA3DC2D29603E369348A8', 'MD5': '4787B628578FA3DC2D29603E369348A8', 'Title': 'The God Delusion', 'Author': 'Richard Dawkins', 'Year': '2006', 'Language': 'English', 'Pages': None, 'ID': '46', 'Size': '343 Kb (351078)', 'Extension': 'chm'}

{'Thumb': 'http://libgen.rs/covers/0/f5e45a4a88744c863385fdf19c9f40ce-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=F5E45A4A88744C863385FDF19C9F40CE', 'MD5': 'F5E45A4A88744C863385FDF19C9F40CE', 'Title': 'How the Mind Works', 'Author': 'Steven Pinker', 'Year': '1999', 'Language': 'English', 'Pages': None, 'ID': '101', 'Size': '3 Mb (3119362)', 'Extension': 'chm'}

{'Thumb': 'http://libgen.rs/covers/0/5fb1eff06867dd2b197943b46b023f0d-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=5FB1EFF06867DD2B197943B46B023F0D', 'MD5': '5FB1EFF06867DD2B197943B46B023F0D', 'Title': 'The blank slate: the modern denial of human nature', 'Author': 'Steven Pinker', 'Year': '2002', 'Language': 'English', 'Pages': None, 'ID': '102', 'Size': '2 Mb (2291483)', 'Extension': 'chm'}

{'Thumb': 'http://libgen.rs/covers/000/bb5a6040d0465fffc8891ccb73027f16-g.jpg', 'Download_link': 'http://libgen.rs/get?&md5=BB5A6040D0465FFFC8891CCB73027F16', 'MD5': 'BB5A6040D0465FFFC8891CCB73027F16', 'Title': '101 ключевая идея: Эволюция: Происхождение жизни. Равновесие Харди-Вайнберга', 'Author': 'Мортон Дженкинс', 'Year': '2001', 'Language': 'Russian', 'Pages': None, 'ID': '194', 'Size': '212 Kb (217222)', 'Extension': 'chm'}

{'Thumb': 'http://libgen.rs/covers/0/67d566396616fd0982d659b6cfc1b664-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=67D566396616FD0982D659B6CFC1B664', 'MD5': '67D566396616FD0982D659B6CFC1B664', 'Title': 'Наглядная биохимия', 'Author': 'Я.Кольман, К.-Г.Рем. Перевод с немецкого Л.В.Козлова, Е.С.Левиной и П.Д.Решетова Под редакцией П.Д.Решетова и Т.И.Соркиной.', 'Year': '2000', 'Language': 'Russian', 'Pages': '469', 'ID': '222', 'Size': '16 Mb (17291435)', 'Extension': 'chm'}
</details>

To search using ISBN of book:

```python3
search_result = libgen.search_isbn("9783935042697")
```

<details>
<summary>output</summary>
{'Thumb': 'http://libgen.rs/covers/2945000/4efa9a991b645f75be61871447c559ca-g.jpg', 'Download_link': 'http://libgen.rs/get?&md5=4EFA9A991B645F75BE61871447C559CA', 'MD5': '4EFA9A991B645F75BE61871447C559CA', 'Title': 'Python Basics: A Practical Introduction to Python 3', 'Author': 'David Amos', 'Year': '2021', 'Language': 'English', 'Pages': None, 'ID': '2945746', 'Size': '6 Mb (6774691)', 'Extension': 'pdf'}
</details>

To search using langauge of book:

```python3
search_result = libgen.search_language("english")
```

<details>
<summary>output</summary>
{'Thumb': 'http://libgen.rs/covers/0/7b2a4d53fde834e801c26a2bab7e0240.jpg', 'Download_link': 'http://libgen.rs/get?&md5=7B2A4D53FDE834E801C26A2BAB7E0240', 'MD5': '7B2A4D53FDE834E801C26A2BAB7E0240', 'Title': 'Handbook of Clinical Drug Data', 'Author': 'Philip Anderson', 'Year': '2001', 'Language': 'English', 'Pages': '1163', 'ID': '1', 'Size': '3 Mb (3627486)', 'Extension': 'pdf'}

{'Thumb': 'http://libgen.rs/covers/0/048ea0496db0444f873139cd705a07af-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=048EA0496DB0444F873139CD705A07AF', 'MD5': '048EA0496DB0444F873139CD705A07AF', 'Title': 'Handbook of Herbs and Spices', 'Author': 'K V Peter', 'Year': '2001', 'Language': 'English', 'Pages': '332', 'ID': '2', 'Size': '1 Mb (1552793)', 'Extension': 'pdf'}

{'Thumb': 'http://libgen.rs/covers/0/411b9300a2f2094800e0e30d439c30fd-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=411B9300A2F2094800E0E30D439C30FD', 'MD5': '411B9300A2F2094800E0E30D439C30FD', 'Title': 'Handbook of Herbs and Spices: Volume 2', 'Author': 'Peter', 'Year': '2004', 'Language': 'English', 'Pages': None, 'ID': '3', 'Size': '2 Mb (2298559)', 'Extension': 'pdf'}

{'Thumb': 'http://libgen.rs/covers/0/372e34d136fbf39dce00460d9e8f1f52.jpg', 'Download_link': 'http://libgen.rs/get?&md5=372E34D136FBF39DCE00460D9E8F1F52', 'MD5': '372E34D136FBF39DCE00460D9E8F1F52', 'Title': 'Medical terminology, an illustrated guide', 'Author': 'Barbara Janson Cohen', 'Year': '2004', 'Language': 'English', 'Pages': '744', 'ID': '4', 'Size': '12 Mb (12287946)', 'Extension': 'djvu'}

{'Thumb': 'http://libgen.rs/covers/0/c086e2244ad712fe683c37c0e677b79b-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=C086E2244AD712FE683C37C0E677B79B', 'MD5': 'C086E2244AD712FE683C37C0E677B79B', 'Title': "Patterson's Allergic Diseases", 'Author': 'Leslie C. Grammer', 'Year': '2002', 'Language': 'English', 'Pages': '509', 'ID': '6', 'Size': '13 Mb (13319483)', 'Extension': 'pdf'}
</details>

To search using publisher of book:

```python3
search_result = libgen.search_publisher("McGraw-Hill")
```

<details>
<summary>output</summary>
{'Thumb': 'http://libgen.rs/covers/0/7b2a4d53fde834e801c26a2bab7e0240.jpg', 'Download_link': 'http://libgen.rs/get?&md5=7B2A4D53FDE834E801C26A2BAB7E0240', 'MD5': '7B2A4D53FDE834E801C26A2BAB7E0240', 'Title': 'Handbook of Clinical Drug Data', 'Author': 'Philip Anderson', 'Year': '2001', 'Language': 'English', 'Pages': '1163', 'ID': '1', 'Size': '3 Mb (3627486)', 'Extension': 'pdf'}

{'Thumb': 'http://libgen.rs/covers/0/5f94ea5f1ebcbf82d9e46ae72bcfaa08-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=5F94EA5F1EBCBF82D9E46AE72BCFAA08', 'MD5': '5F94EA5F1EBCBF82D9E46AE72BCFAA08', 'Title': "Schaum's Immunology", 'Author': 'George Pinchuk', 'Year': '2001', 'Language': 'English', 'Pages': '329', 'ID': '8', 'Size': '4 Mb (4077170)', 'Extension': 'djvu'}

{'Thumb': 'http://libgen.rs/covers/0/cff0dece0fbc9780f3c13daf1936dab7-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=CFF0DECE0FBC9780F3C13DAF1936DAB7', 'MD5': 'CFF0DECE0FBC9780F3C13DAF1936DAB7', 'Title': 'Microbiology demystified', 'Author': 'Tom Betsy', 'Year': '2005', 'Language': 'English', 'Pages': '309', 'ID': '27', 'Size': '3 Mb (2958038)', 'Extension': 'pdf'}

{'Thumb': 'http://libgen.rs/covers/0/c924f24882bb6b47d55131f6a373f5c7-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=C924F24882BB6B47D55131F6A373F5C7', 'MD5': 'C924F24882BB6B47D55131F6A373F5C7', 'Title': "Schaum's outline of theory and problems of biochemistry", 'Author': 'Philip Kuchel', 'Year': '1998', 'Language': 'English', 'Pages': '572', 'ID': '73', 'Size': '6 Mb (6639413)', 'Extension': 'djvu'}

{'Thumb': 'http://libgen.rs/covers/0/a50f2e8f2963888a976899e2c4675d70.jpg', 'Download_link': 'http://libgen.rs/get?&md5=A50F2E8F2963888A976899E2C4675D70', 'MD5': 'A50F2E8F2963888A976899E2C4675D70', 'Title': 'Physiology demystified', 'Author': 'Layman D.P.', 'Year': '2004', 'Language': 'English', 'Pages': '432', 'ID': '76', 'Size': '9 Mb (9364185)', 'Extension': 'pdf'}
</details>

To search using tags of book:

```python3
search_result = libgen.search_tag("programming")
```

<details>
<summary>output</summary>
{'Thumb': 'http://libgen.rs/covers/0/6066c1b029ada93730b364c1592fb015-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=6066C1B029ADA93730B364C1592FB015', 'MD5': '6066C1B029ADA93730B364C1592FB015', 'Title': 'Combinatorics on Traces', 'Author': 'Volker Diekert (auth.)', 'Year': '1990', 'Language': 'English', 'Pages': None, 'ID': '751', 'Size': '1 Mb (1270783)', 'Extension': 'djvu'}

{'Thumb': 'http://libgen.rs/covers/0/77ea2db71148f51d42628e66cbf612c9-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=77EA2DB71148F51D42628E66CBF612C9', 'MD5': '77EA2DB71148F51D42628E66CBF612C9', 'Title': 'Efficient Graph Rewriting and Its Implementation', 'Author': 'Heiko Dörr (eds.)', 'Year': '1995', 'Language': 'English', 'Pages': None, 'ID': '752', 'Size': '2 Mb (2228318)', 'Extension': 'djvu'}

{'Thumb': 'http://libgen.rs/covers/0/8ae5c7bf5dee99bfa7d339b35456e892-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=8AE5C7BF5DEE99BFA7D339B35456E892', 'MD5': '8AE5C7BF5DEE99BFA7D339B35456E892', 'Title': 'Advanced Functional Programming: Second International School Olympia, WA, USA, August 26–30, 1996 Tutorial Text', 'Author': 'Sigbjorn Finne', 'Year': '1996', 'Language': 'English', 'Pages': '244', 'ID': '785', 'Size': '2 Mb (1979590)', 'Extension': 'djvu'}

{'Thumb': 'http://libgen.rs/covers/1000/7bec16add82336b72fbd6db17811940a-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=7BEC16ADD82336B72FBD6DB17811940A', 'MD5': '7BEC16ADD82336B72FBD6DB17811940A', 'Title': 'Filtering, Segmentation and Depth', 'Author': 'Mark Nitzberg', 'Year': '1993', 'Language': 'English', 'Pages': None, 'ID': '1342', 'Size': '1 Mb (1418351)', 'Extension': 'djvu'}

{'Thumb': 'http://libgen.rs/covers/1000/064e4f885885efcef70ee17fa51a3b11-d.jpg', 'Download_link': 'http://libgen.rs/get?&md5=064E4F885885EFCEF70EE17FA51A3B11', 'MD5': '064E4F885885EFCEF70EE17FA51A3B11', 'Title': "Implementation of Functional Languages: 8th International Workshop, IFL'96 Bad Godesberg, Germany, September 16–18, 1996 Selected Papers", 'Author': 'Lee Braine', 'Year': '1997', 'Language': 'English', 'Pages': None, 'ID': '1502', 'Size': '3 Mb (2673640)', 'Extension': 'djvu'}
</details>

### Download stuff

To get direct download link of book, use its MD5 specifier as follows:

```python3
download_url = libgen.resolve_download_link(md5="6066C1B029ADA93730B364C1592FB015")
```

<details>
<summary>output</summary>
https://cloudflare-ipfs.com/ipfs/bafykbzaceaovkuyhyugtrvmngqda4zfbxsi4hg7bz6va3odthmdoifaf23glk?filename=%28Lecture%20Notes%20in%20Computer%20Science%20454%29%20Volker%20Diekert%20%28auth.%29%20-%20Combinatorics%20on%20Traces-Springer-Verlag%20Berlin%20Heidelberg%20%281990%29.djvu
</details>

To download the book, use its MD5 identifier as follows:

```python3
# path can be an absolute or full path.
# Needs to be a valid path and should end with a valid file name with its respective extension.
# Name of file can be determined by you, extension must be taken from the search results.

libgen.download(md5="6066C1B029ADA93730B364C1592FB015", path="./books/6066C1B029ADA93730B364C1592FB015.djvu")
```

<details>
<summary>output</summary>
<img src="https://raw.githubusercontent.com/BeastImran/libgenparser/main/download_output.jpg"/></a>
</details>

## Final words

Hope this project made your life a little easier. Any contribution? pm me in [telegram](https://t.me/beastimran).
