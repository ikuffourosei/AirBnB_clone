#!/usr/bin/python3
"""the __init__ file"""


from .engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
