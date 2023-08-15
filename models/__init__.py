#!/usr/bin/python3
"""__init__ create a unique FileStorage instance for my application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
