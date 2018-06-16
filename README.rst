===============
alphabetmatcher
===============


.. image:: https://img.shields.io/pypi/v/alphabetmatcher.svg
        :target: https://pypi.python.org/pypi/alphabetmatcher

.. image:: https://img.shields.io/travis/natemarks/alphabetmatcher.svg
        :target: https://travis-ci.org/natemarks/alphabetmatcher

.. image:: https://readthedocs.org/projects/alphabetmatcher/badge/?version=latest
        :target: https://alphabetmatcher.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status



Problem:
You will receive a string as input, potentially a mixture of upper and lower case, numbers, special characters etc. The task is to determine if the string contains at least one of each letter of the alphabet. Return true if all are found and false if not. Write it as a RESTful web service (no authentication necessary) in any language/framework you choose and document the service.


app.py runs a Flask rest server that accepts POST requests on http://localhost:5000/matcher.  POSTed data is passed as an init parameter to instantiate alphabetmatcher.Matcher.  All the matching logic is contained in the Matcher class and the success or failure of the match is returned from Matcher.success().

The rest app converts the boolean output of success to a string and returns it to the requestor

the tests in test_alphabetmatcher.py only test the matching logic in alphabetmatcher.Matcher directly

The tests in test_app.py run the flask REST listener and test the matcher through the REST interface


* Free software: MIT license
* Documentation: https://alphabetmatcher.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


i used this article to put together my first REST application:
https://sourcedexter.com/python-rest-api-flask/


I used this article as a rference for starting the REST listener as a pytest fixture

https://serge-m.github.io/testing-json-responses-in-Flask-REST-apps-with-pytest.html

