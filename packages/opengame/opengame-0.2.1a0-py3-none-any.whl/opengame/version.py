from collections import namedtuple

__all__ = ['version', 'get_string']

_Version = namedtuple('Version', ['major', 'minor', 'micro'])
version = _Version(0, 2, 1)

def get_string():
    return '.'.join(map(str, version))
