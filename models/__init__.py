#!/usr/bin/python3
"""models package init file"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
