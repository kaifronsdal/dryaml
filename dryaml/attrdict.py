"""
A dictionary wrapper that allows accessing keys as attributes. This simplifies
accessing YAML data, which is often a nested dictionary.

Example
-------
>>> from dryaml import AttrDict
>>> d = AttrDict({'a': 1, 'b': {'c': 2}})
>>> d.a
1
>>> d.b.c, d['b']['c'], d['b'].c
(2, 2, 2)
"""
from typing import Any, Dict, Optional, Union

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)