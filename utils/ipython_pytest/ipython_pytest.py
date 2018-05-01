import os
import shlex
import sys
from pathlib import Path

import tempfile
from IPython.core import magic
from pytest import main as pytest_main


TEST_MODULE_NAME = '_ipytesttmp'

def pytest(line, cell):
    with tempfile.TemporaryDirectory() as root:
        oldcwd = os.getcwd()
        os.chdir(root)
        tests_module_path = '{}.py'.format(TEST_MODULE_NAME)
        try:
            Path(tests_module_path).write_text(cell)
            args = shlex.split(line)
            os.environ['COLUMNS'] = '80'
            pytest_main(args + [tests_module_path])
            if TEST_MODULE_NAME in sys.modules:
                del sys.modules[TEST_MODULE_NAME]
        finally:
            os.chdir(oldcwd)

def load_ipython_extension(ipython):
    magic.register_cell_magic(pytest)
