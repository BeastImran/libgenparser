from libgenparser.__future__.parser import *

try:
    import cache
except Exception:
    raise ImportError('`async-cache` module is not install to cache async methods!. pip install async-cache')

__title__ = "Libgen-Parser"
__version__ = "0.1.0"
__author__ = "Shaik Imran"
