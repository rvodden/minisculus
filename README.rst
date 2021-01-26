Richard Vodden's attempt at the minisculus challenge
====================================================

See here: http://minisculuschallenge.com/index.html for more information!

To build the documentation, spin up a virtual environment using you favourite implementation, install the prereqs from ``requirements.txt`` and then run ``nox -s docs``. For example on a mac using virtualenv:

.. code-block::

    > virtualenv .venv
    > . .venv/bin/activate
    > pip install -r requirements.txt
    > nox -s docs
    > open docs/_build/index.html
