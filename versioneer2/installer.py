# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import codecs

import versioneer2

file_to_copy = versioneer2.__file__
version = versioneer2.__version__

del versioneer2

def main():
    versioneer_init = codecs.open(file_to_copy, 'r', encoding='utf-8').read()
    # Manually overwrite the version string
    versioneer_py = versioneer_init.replace(u"""\
# Versioneer versioning
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions""", "__version__ = {}".format(version.decode('utf-8')))

    if os.path.exists("versioneer.py"):
        print("overwriting existing versioneer.py")
    with codecs.open("versioneer.py", 'w', encoding='utf-8') as f:
        f.write(versioneer_py)
    print("versioneer.py ({0}) installed into local tree".format(
        version))
    print("Now please follow instructions in the docstring.")
