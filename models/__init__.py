#!/usr/bin/python3
"""the __init__ file"""


from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
