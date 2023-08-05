#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 21:21:11 2022

@author: mike
"""
# import logging
from collections.abc import Mapping, MutableMapping
import gzip
# from sys import exit
from typing import Any, Generic, Iterator, Union
import lmdb
import pickle
import json

imports = {}
try:
    import orjson
    imports['orjson'] = True
except:
    imports['orjson'] = False

try:
    import zstandard as zstd
    imports['zstd'] = True
except:
    imports['zstd'] = False

try:
    import lz4
    imports['lz4'] = True
except:
    imports['lz4'] = False

# try:
#     import numpy as np
#     imports['numpy'] = True
# except:
#     imports['numpy'] = False

from . import utils
# import utils

# logger = logging.getLogger(__name__)

#######################################################
### Serializers and compressors

## Serializers
class Pickle:
    def __init__(self, protocol):
        self.protocol = protocol
    def dumps(self, obj):
        return pickle.dumps(obj, self.protocol)
    def loads(self, obj):
        return pickle.loads(obj)


class Json:
    def dumps(obj: Any) -> bytes:
        return json.dumps(obj).encode()
    def loads(obj):
        return json.loads(obj.decode())


class Orjson:
    def dumps(obj: Any) -> bytes:
        return orjson.dumps(obj, option=orjson.OPT_NON_STR_KEYS | orjson.OPT_OMIT_MICROSECONDS | orjson.OPT_SERIALIZE_NUMPY)
    def loads(obj):
        return orjson.loads(obj)


# class Numpy:
#     def dumps(obj: np.ndarray) -> bytes:
#         return json.dumps(obj).tobytes()
#     def loads(obj):
#         return np.frombuffer(obj)


## Compressors
class Gzip:
    def __init__(self, compress_level):
        self.compress_level = compress_level
    def compress(self, obj):
        return gzip.compress(obj, self.compress_level)
    def decompress(self, obj):
        return gzip.decompress(obj)


class Zstd:
    def __init__(self, compress_level):
        self.compress_level = compress_level
    def compress(self, obj):
        return zstd.compress(obj, self.compress_level)
    def decompress(self, obj):
        return zstd.decompress(obj)


class Lz4:
    def __init__(self, compress_level):
        self.compress_level = compress_level
    def compress(self, obj):
        return zstd.compress(obj, self.compress_level)
    def decompress(self, obj):
        return zstd.decompress(obj)


#######################################################
### Classes


class Shock(MutableMapping):

    def __init__(self, file_path: str, flag: str = "r", map_size: int = 2**40, lock: bool = False, sync: bool = False, max_readers: int = 126, serializer: str = None, protocol: int = 5, compressor: str = None, compress_level: int = 1):
        """

        """
        ## Open lmdb
        if flag == "r":  # Open existing database for reading only (default)
            env = lmdb.open(file_path, map_size=map_size, max_dbs=0, readonly=True, create=False, subdir=False, lock=lock, sync=False, max_readers=max_readers)
            write = False
        elif flag == "w":  # Open existing database for reading and writing
            env = lmdb.open(file_path, map_size=map_size, max_dbs=0, readonly=False, create=False, subdir=False, lock=lock, sync=sync, max_readers=max_readers)
            write = True
        elif flag == "c":  # Open database for reading and writing, creating it if it doesn't exist
            env = lmdb.open(file_path, map_size=map_size, max_dbs=0, readonly=False, create=True, subdir=False, lock=lock, sync=sync, max_readers=max_readers)
            write = True
        elif flag == "n":  # Always create a new, empty database, open for reading and writing
            utils.remove_db(file_path)
            env = lmdb.open(file_path, map_size=map_size, max_dbs=0, readonly=False, create=True, subdir=False, lock=lock, sync=sync, max_readers=max_readers)
            write = True
        else:
            raise ValueError("Invalid flag")

        self.env = env
        self._write = write

        ## Serializer
        if serializer is None:
            self._serializer = None
        elif serializer == 'pickle':
            self._serializer = Pickle(protocol)
        elif serializer == 'json':
            self._serializer = Json
        elif serializer == 'orjson':
            if imports['orjson']:
                self._serializer = Orjson
            else:
                raise ValueError('orjson could not be imported.')
        else:
            raise ValueError('serializer must be one of pickle, json, or orjson.')

        ## Compressor
        if compressor is None:
            self._compressor = None
        elif compressor == 'gzip':
            self._compressor = Gzip(compress_level)
        elif compressor == 'zstd':
            if imports['zstd']:
                self._compressor = Zstd(compress_level)
            else:
                raise ValueError('zstd could not be imported.')
        elif compressor == 'lz4':
            if imports['lz4']:
                self._compressor = Lz4(compress_level)
            else:
                raise ValueError('lz4 could not be imported.')


    def info(self) -> dict:
        """
        Return some lmdb environment information.

        Returns
        -------
        dict
        """
        return self.env.info()

    def set_map_size(self, value: int) -> None:
        """
        Change the map size of the database by a value.
        """

        self.env.set_mapsize(value)

    def copy(self, file_path, compact=True):
        """
        Make a consistent copy of the environment in the given destination file path.

        Parameters
        ----------
        file_path : str or path-like
            Path to new file.
        compact:
            If True, perform compaction while copying: omit free pages and sequentially renumber all pages in output. This option consumes more CPU and runs more slowly than the default, but may produce a smaller output database.
        """
        self.env.copy(file_path, compact=compact)


    def _pre_key(self, key: str) -> bytes:

        return key.encode()

    def _post_key(self, key: bytes) -> str:

        return key.decode()

    def _pre_value(self, value) -> bytes:

        ## Serialize to bytes
        if self._serializer is not None:
            value = self._serializer.dumps(value)

        ## Compress bytes
        if self._compressor is not None:
            value = self._compressor.compress(value)

        return value

    def _post_value(self, value: bytes):

        ## Decompress bytes
        if self._compressor is not None:
            value = self._compressor.decompress(value)

        ## Serialize from bytes
        if self._serializer is not None:
            value = self._serializer.loads(value)

        return value

    def __getitem__(self, key: str):

        with self.env.begin(write=False, buffers=False) as txn:
            value = txn.get(self._pre_key(key))

        if value is None:
            raise KeyError(key)
        return self._post_value(value)

    def __setitem__(self, key: str, value) -> None:
        if self._write:
            with self.env.begin(write=True, buffers=False) as txn:
                txn.put(self._pre_key(key), self._pre_value(value))
        else:
            raise ValueError('File is open for read only.')

    def __delitem__(self, key: str) -> None:
        if self._write:
            with self.env.begin(write=True, buffers=False) as txn:
                txn.delete(self._pre_key(key))
        else:
            raise ValueError('File is open for read only.')

    def keys(self):

        with self.env.begin(write=False, buffers=False) as txn:
            for key in txn.cursor().iternext(keys=True, values=False):
                yield self._post_key(key)

    def items(self):

        with self.env.begin(write=False, buffers=False) as txn:
            for key, value in txn.cursor().iternext(keys=True, values=True):
                yield (self._post_key(key), self._post_value(value))

    def values(self):

        with self.env.begin(write=False, buffers=False) as txn:
            for value in txn.cursor().iternext(keys=False, values=True):
                yield self._post_value(value)

    def __contains__(self, key: str) -> bool:

        with self.env.begin(write=False, buffers=False) as txn:
            return txn.cursor().set_key(self._pre_key(key))

    def __iter__(self):

        return self.keys()

    def __len__(self) -> int:

        with self.env.begin(write=False, buffers=False) as txn:
            return txn.stat()["entries"]

    def pop(self, key: str, default=None):

        if self._write:
            with self.env.begin(write=True, buffers=False) as txn:
                value = txn.pop(self._pre_key(key))
        else:
            raise ValueError('File is open for read only.')

        if value is None:
            if default is None:
                raise KeyError(key)
            else:
                return default

        return self._post_value(value)

    def update(self, dict):
        """

        """
        if self._write:
            with self.env.begin(write=True, buffers=False) as txn:
                for key, value in dict.items():
                    txn.put(self._pre_key(key), self._pre_value(value))
        else:
            raise ValueError('File is open for read only.')


    # The method "drop" should work for this without iterating through all objects
    def clear(self):
        if self._write:
            with self.env.begin(write=True, buffers=False) as txn:
                for key in txn.cursor().iternext(keys=True, values=False):
                    txn.delete(key)
        else:
            raise ValueError('File is open for read only.')
        # if self._write:
        #     with self.env.begin(write=True, buffers=False) as txn:
        #         txn.drop(db=None, delete=delete)
        # else:
        #     raise ValueError('File is open for read only.')


    def sync(self) -> None:
        """
        Flush the data buffers to disk. Must be performed after a series of writes.
        """
        if self._write:
            self.env.sync()

    def close(self) -> None:
        """
        Close the environment, invalidating non-synced writes.
        """
        self.sync()
        self.env.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def open(
    file_path: str, flag: str = "r", map_size: int = 2**40, lock: bool = False, sync: bool = False, max_readers: int = 126, serializer: str = None, protocol: int = 5, compressor: str = None, compress_level: int = 1):
    """
    Open a persistent dictionary for reading and writing.

    Parameters
    -----------
    file_path : str or pathlib.Path
        It must be a path to a local file location.
    flag : str
        Flag associated with how the file is opened according to the dbm style. See below for details.
    map_size : int
        Maximum size database may grow to; used to size the memory mapping. If database grows larger than map_size, an exception will be raised and the user must close and reopen Environment. On 64-bit there is no penalty for making this huge (say 1TB). Must be <2GB on 32-bit.
    lock : bool
        If False, don’t do any locking. If concurrent access is anticipated, the caller must manage all concurrency itself. For proper operation the caller must enforce single-writer semantics, and must ensure that no readers are using old transactions while a writer is active. The simplest approach is to use an exclusive lock so that no readers may be active at all when a writer begins.
    sync : bool
        If False, don’t flush system buffers to disk when committing a transaction. This optimization means a system crash can corrupt the database or lose the last transactions if buffers are not yet flushed to disk.

The risk is governed by how often the system flushes dirty buffers to disk and how often sync() is called. However, if the filesystem preserves write order, transactions exhibit ACI (atomicity, consistency, isolation) properties and only lose D (durability). I.e. database integrity is maintained, but a system crash may undo the final transactions.
    max_readers : int
        Maximum number of simultaneous read transactions. Can only be set by the first process to open an environment, as it affects the size of the lock file and shared memory area. Attempts to simultaneously start more than this many read transactions will fail.
    serializer : str or None
        The serializer to use to convert the input object to bytes. Currently, must be one of pickle, json, orjson, or None. If the objects can be serialized to json, then use orjson. It's super fast and you won't have the pickle issues.
        If None, then the input values must be bytes.
    protocol : int
        The pickle protocol to use.
    compressor : str or None
        The compressor to use to compress the pickle object before being written. Currently, only zstd is accepted.
        The amount of compression will vary wildly depending on the input object and the serializer used. It's definitely worth doing some testing before using a compressor. Saying that...if you serialize to json, you'll likely get a lot of benefit from a fast compressor.
    compress_level : int
        The compression level for the compressor.

    Returns
    -------
    Shock

    The optional *flag* argument can be:

   +---------+-------------------------------------------+
   | Value   | Meaning                                   |
   +=========+===========================================+
   | ``'r'`` | Open existing database for reading only   |
   |         | (default)                                 |
   +---------+-------------------------------------------+
   | ``'w'`` | Open existing database for reading and    |
   |         | writing                                   |
   +---------+-------------------------------------------+
   | ``'c'`` | Open database for reading and writing,    |
   |         | creating it if it doesn't exist           |
   +---------+-------------------------------------------+
   | ``'n'`` | Always create a new, empty database, open |
   |         | for reading and writing                   |
   +---------+-------------------------------------------+

    """

    return Shock(file_path, flag, map_size, lock, sync, max_readers, serializer, protocol, compressor, compress_level)



# for key, value in shock0.items():
#     print(key)



# def multitest(db, key, data):
#     db[key] = data
    # db.sync()


# def multitest(file_path, key, data):
#     with open(file_path, 'w', lock=True) as db:
#         db[key] = data
