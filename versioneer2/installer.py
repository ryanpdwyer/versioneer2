# -*- coding: utf-8 -*-
import os
import versioneer2

def main():
    versioneer_init = open(versioneer2.__file__, 'rb').read()
    # Manually overwrite the version string
    versioneer_py = versioneer_init.replace("""\
# Versioneer versioning
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions""", "__version__ = {}".format(versioneer2.__version__))

    if os.path.exists("versioneer.py"):
        print("overwriting existing versioneer.py")
    with open("versioneer.py", "wb") as f:
        f.write(versioneer_py)
    print("versioneer.py ({0}) installed into local tree".format(__version__))
    print("Now please follow instructions in the docstring.")
