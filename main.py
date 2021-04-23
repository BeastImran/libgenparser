from time import time

from libgenparser.parser import LibgenParser

libgen = LibgenParser()

t1 = time()
title_data = libgen.search_title("advanced python")
print(title_data)
print(time() - t1)

t1 = time()
md5_data = libgen.search_md5(title_data[0].get('MD5'))
print(md5_data)
print(time() - t1)

t1 = time()
title_data = libgen.search_title("advanced python")
print(title_data)
print(time() - t1)

t1 = time()
md5_data = libgen.search_md5(title_data[0].get('MD5'))
print(md5_data)
print(time() - t1)

print("ASYNC VERSION")
from libgenparser.__future__.parser import LibgenParser as AyncLibgenParser
import asyncio


async def async_main():
    libgen = AyncLibgenParser()

    t1 = time()
    title_data = await libgen.search_title("advanced python")
    print(title_data)
    print(time() - t1)

    t1 = time()
    md5_data = await libgen.search_md5(title_data[0].get('MD5'))
    print(md5_data)
    print(time() - t1)

    t1 = time()
    title_data = await libgen.search_title("advanced python")
    print(title_data)
    print(time() - t1)

    t1 = time()
    md5_data = await libgen.search_md5(title_data[0].get('MD5'))
    print(md5_data)
    print(time() - t1)


asyncio.run(async_main())
