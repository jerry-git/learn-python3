ipython_pytest
--------------

This little IPython extension gives you the ability to
run tests using Pytest in an IPython Notebook.

The motivation for the extension was to make it possible to
demonstrate test-driven development using pytest in an IPython
notebook driven presentation.

This extension does not attempt to enable using notebooks as test
suites. The intention is also not to collect test results from
multiple cells, but to do separate test runs for cells in an
interactive presentation.

This extension attempts to achieve for pytest_ what the
`ipython_nose`_ extension does for nose_. Unfortunately it isn't able
to inject globals from the notebook environment into the test like the
``%%nose`` cell magic in `ipython_nose_`. Instead, in
``ipython_pytest``, all imports, constants and helper functions need
to be contained in the test cell itself.

.. _pytest: https://pytest.org/
.. _ipython_nose: https://github.com/taavi/ipython_nose/pull/11/files
.. _nose: https://nose.readthedocs.io/


Installation
------------

* Make sure your IPython Notebook server can import ``ipython_pytest.py`` (e.g.
  copy it to a directory in your ``PYTHONPATH``, or modify ``PYTHONPATH``
  before starting IPython Notebook). It's also probably sufficient to have
  ``ipython_pytest.py`` in the directory from which you run the notebook, e.g.::

    $ ls
    ipython_pytest.py
    $ ipython notebook

* You can also install it in a virtualenv in developent mode::

    $ cd ipython-pytest
    $ pip install -e .


Usage
-----

* Add a cell containing::

    %load_ext ipython_pytest

  somewhere in your notebook.

* Write tests that conform to Pytest conventions, e.g.::

    def test_arithmetic():
        assert 1+1 == 2

* Add a cell consisting of::

    %%pytest

    def test_my_stuff():
        assert 42 == 42

  to your notebook and run that cell. That will discover your
  ``test_*`` functions, run them, and show console output from
  Pytest.

* Pass standard Pytest arguments to the magic::

    %%pytest --tb=short


Caveats
-------

* None of the objects defined in other cells of the notebook are available
  in the test cell.


Authors
-------

* Antti Kaihola <antti dot kaihola at eniram dot fi>

Thanks to Taavi Burns for the idea in his ipython-nose package.


Get the code
------------

::

  git clone https://github.com/akaihola/ipython_pytest.git


Copyright
---------

Copyright (c) 2016, Antti Kaihola.

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

Neither the name of the developers nor the names of contributors may
be used to endorse or promote products derived from this software
without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
