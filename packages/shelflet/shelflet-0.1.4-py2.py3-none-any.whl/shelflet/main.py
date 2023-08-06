#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Manage shelves of pickled objects...now with compression!

A "shelf" is a persistent, dictionary-like object.  The difference
with dbm databases is that the values (not the keys!) in a shelf can
be essentially arbitrary Python objects -- anything that the "pickle"
module can handle.  This includes most class instances, recursive data
types, and objects containing lots of shared sub-objects.  The keys
are ordinary strings.

To summarize the interface (key is a string, data is an arbitrary
object):

        import shelve
        d = shelve.open(filename) # open, with (g)dbm filename -- no suffix

        d[key] = data   # store data at key (overwrites old data if
                        # using an existing key)
        data = d[key]   # retrieve a COPY of the data at key (raise
                        # KeyError if no such key) -- NOTE that this
                        # access returns a *copy* of the entry!
        del d[key]      # delete data stored at key (raises KeyError
                        # if no such key)
        flag = key in d # true if the key exists
        list = d.keys() # a list of all existing keys (slow!)

        d.close()       # close it

Dependent on the implementation, closing a persistent dictionary may
or may not be necessary to flush changes to disk.

Normally, d[key] returns a COPY of the entry.  This needs care when
mutable entries are mutated: for example, if d[key] is a list,
        d[key].append(anitem)
does NOT modify the entry d[key] itself, as stored in the persistent
mapping -- it only modifies the copy, which is then immediately
discarded, so that the append has NO effect whatsoever.  To append an
item to d[key] in a way that will affect the persistent mapping, use:
        data = d[key]
        data.append(anitem)
        d[key] = data

To avoid the problem with mutable entries, you may pass the keyword
argument writeback=True in the call to shelve.open.  When you use:
        d = shelve.open(filename, writeback=True)
then d keeps a cache of all entries you access, and writes them all back
to the persistent mapping when you call d.close().  This ensures that
such usage as d[key].append(anitem) works as intended.

However, using keyword argument writeback=True may consume vast amount
of memory for the cache, and it may make d.close() very slow, if you
access many of d's entries after opening it in this way: d has no way to
check which of the entries you access are mutable and/or which ones you
actually mutate, so it must cache, and write back at close, all of the
entries that you access.  You can call d.sync() to write back all the
entries in the cache, and empty the cache (d.sync() also synchronizes
the persistent dictionary on disk, if feasible).
"""
import pickle
import _gdbm as dbm
import pickle
import json
import pathlib
import inspect
import gzip
from collections.abc import Mapping, MutableMapping
from typing import Any, Generic, Iterator, Union

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


__all__ = ["Shelf", "open"]

hidden_keys = (b'00~._serializer', b'01~._compressor')

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
        return lz4.frame.compress(obj, self.compress_level)
    def decompress(self, obj):
        return lz4.frame.decompress(obj)


#######################################################
### Classes

class _ClosedDict(MutableMapping):
    'Marker for a closed dict.  Access attempts raise a ValueError.'

    def closed(self, *args):
        raise ValueError('invalid operation on closed shelf')
    __iter__ = __len__ = __getitem__ = __setitem__ = __delitem__ = keys = closed

    def __repr__(self):
        return '<Closed Dictionary>'


class Shelf(MutableMapping):
    """Base class for shelf implementations.

    This is initialized with a dictionary-like object.
    See the module's __doc__ string for an overview of the interface.
    """

    def __init__(self, file_path: str, flag: str = "r", sync: bool = False, lock: bool = True, serializer = None, protocol: int = 5, compressor = None, compress_level: int = 1):
        """

        """
        if flag == "r":  # Open existing database for reading only (default)
            write = False
            fp_exists = True
        elif flag == "w":  # Open existing database for reading and writing
            write = True
            fp_exists = True
        elif flag == "c":  # Open database for reading and writing, creating it if it doesn't exist
            fp = pathlib.Path(file_path)
            fp_exists = fp.exists()
            write = True
        elif flag == "n":  # Always create a new, empty database, open for reading and writing
            write = True
            fp_exists = False
        else:
            raise ValueError("Invalid flag")

        if sync:
            extra_flag = 's'
        else:
            extra_flag = 'f'
        env = dbm.open(str(file_path), flag+extra_flag)

        self.env = env
        self._write = write

        ## Load or assign encodings
        if fp_exists:
            self._serializer = pickle.loads(env[b'00~._serializer'])
            self._compressor = pickle.loads(env[b'01~._compressor'])
        else:
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
            elif inspect.isclass(serializer):
                class_methods = dir(serializer)
                if ('dumps' in class_methods) and ('loads' in class_methods):
                    self._serializer = serializer
                else:
                    raise ValueError('If a class is passed for a serializer, then it must have dumps and loads methods.')
            else:
                raise ValueError('serializer must be one of pickle, json, orjson, or a serializer class with dumps and loads methods.')

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
            elif inspect.isclass(compressor):
                class_methods = dir(compressor)
                if ('compress' in class_methods) and ('decompress' in class_methods):
                    self._compressor = compressor(compress_level)
                else:
                    raise ValueError('If a class is passed for a compressor, then it must have compress and decompress methods as well as a compress_level parameter in the __init__.')
            else:
                raise ValueError('compressor must be one of gzip, zstd, lz4, or a compressor class with compress and decompress methods.')

            ## Save encodings if new file
            env[b'00~._serializer'] = pickle.dumps(self._serializer, protocol)
            env[b'01~._compressor'] = pickle.dumps(self._compressor, protocol)

            if hasattr(env, 'sync'):
                env.sync()

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

    def keys(self):
        for key in self.env.keys():
            if key not in hidden_keys:
                yield self._post_key(key)

    def items(self):
        for key in self.env.keys():
            if key not in hidden_keys:
                yield self._post_key(key), self._post_value(self.env[key])

    def values(self):
        for key in self.env.keys():
            if key not in hidden_keys:
                yield self._post_value(self.env[key])

    def __iter__(self):
        return self.keys()

    def __len__(self):
        return len(self.env) - len(hidden_keys)

    def __contains__(self, key):
        return self._pre_key(key) in self.env

    def get(self, key, default=None):
        if self._pre_key(key) in self.env:
            return self._post_value(self.env[self._pre_key(key)])
        return default

    def update(self, key_value_dict):
        """
        Update method only for compatability with dicts. It's no faster than iteratively assigning keys to values.
        """
        if self._write:
            for key, value in key_value_dict.items():
                self[key] = value

            self.sync()
        else:
            raise ValueError('File is open for read only.')

    def reorganize(self):
        """
        Only applies to gdbm.
        If you have carried out a lot of deletions and would like to shrink the space used by the gdbm file, this routine will reorganize the database. gdbm objects will not shorten the length of a database file except by using this reorganization; otherwise, deleted file space will be kept and reused as new (key, value) pairs are added.
        """
        if hasattr(self.env, 'reorganize'):
            self.env.reorganize()
        else:
            raise ValueError('reorganize is unavailable.')
        return

    def __getitem__(self, key):
        value = self.env[self._pre_key(key)]

        return self._post_value(value)

    def __setitem__(self, key, value):
        if self._write:
            self.env[self._pre_key(key)] = self._pre_value(value)
        else:
            raise ValueError('File is open for read only.')

    def __delitem__(self, key):
        del self.env[self._pre_key(key)]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def clear(self):
        if self._write:
            for key in self.keys():
                del self.env[key]
            self.sync()
        else:
            raise ValueError('File is open for read only.')

    def close(self):
        if self.env is None:
            return
        try:
            self.sync()
            try:
                self.env.close()
            except AttributeError:
                pass
        finally:
            # Catch errors that may happen when close is called from __del__
            # because CPython is in interpreter shutdown.
            try:
                self.env = _ClosedDict()
            except:
                self.env = None

    def __del__(self):
        self.close()

    def sync(self):
        if hasattr(self.env, 'sync'):
            self.env.sync()


def open(
    file_path: str, flag: str = "r", sync: bool = False, lock: bool = True, serializer = None, protocol: int = 5, compressor = None, compress_level: int = 1):
    """
    Open a persistent dictionary for reading and writing. On creation of the file, the encodings (serializer and compressor) will be written to the file. Any reads and new writes do not need to be opened with the encoding parameters. Currently, ShockDB uses pickle to serialize the encodings to the file.

    Parameters
    -----------
    file_path : str or pathlib.Path
        It must be a path to a local file location.

    flag : str
        Flag associated with how the file is opened according to the dbm style. See below for details.

    serializer : str, class, or None
        The serializer to use to convert the input object to bytes. Currently, must be one of pickle, json, orjson, or None. If the objects can be serialized to json, then use orjson. It's super fast and you won't have the pickle issues.
        If None, then the input values must be bytes.
        A class with dumps and loads methods can also be passed as a custom serializer.

    protocol : int
        The pickle protocol to use.

    compressor : str, class, or None
        The compressor to use to compress the pickle object before being written. Currently, only zstd is accepted.
        The amount of compression will vary wildly depending on the input object and the serializer used. It's definitely worth doing some testing before using a compressor. Saying that...if you serialize to json, you'll likely get a lot of benefit from a fast compressor.
        A class with compress and decompress methods can also be passed as a custom serializer. The class also needs a compress_level parameter in the __init__.

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

    return Shelf(file_path, flag, sync, lock, serializer, protocol, compressor, compress_level)
