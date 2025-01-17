#!/usr/bin/env python3

import os
import sys

if __name__=="__main__":
    pyc_path = "/tmp/hidden_4.pyc"


    if not os.path.exists(pyc_path):
        print(f"File not found: {pyc_path}")
        sys.exit(1)

    
    import importlib.util

    spec = importlib.util.spec_from_file_location("hidden_4", pyc_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    names.sort()

    for name in names:
        print(name)
