#!/usr/bin/python3
'''initializes the storage engine for models
...

Variables
---------
storage
    a storage engine to manage persistence. An instance
    of ``FileStorage``
'''

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
