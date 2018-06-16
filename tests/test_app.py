#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `alphabetmatcher` package."""


import pytest
from alphabetmatcher.app import app


@pytest.fixture
def client():
    test_client = app.test_client()

    def teardown():
        pass

    # I didn't follow this import in the example
    # request.addfinalizer(teardown)
    return test_client


def test_rest_post():
    import requests

    url = "http://localhost:5000/matcher"
    data = '{"matcher_input":"abcdefghijklmnopqrstuvwxyz"}'

    response = requests.post(url, data=data)

    assert response.content == 'True'