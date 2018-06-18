#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `alphabetmatcher` package."""

import json
import pytest
from alphabetmatcher.app import app


def json_request(client, url, json_dict):
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')


def json_response(response):
    return json.loads(response.data.decode('utf8'))


@pytest.fixture
def client():
    test_client = app.test_client()

    def teardown():
        pass

    # I didn't follow this import in the example
    # request.addfinalizer(teardown)
    return test_client


def test_pos_rest_post(client):
    import requests

    response = json_request(client, '/matcher', {'matcher_input': 'abcdefghijklmnopqrstuvwxyz'})
    # url = "http://localhost:5000/matcher"
    # data = '{"matcher_input":"abcdefghijklmnopqrstuvwxyz"}'

    # response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.data == 'True'


def test_neg_rest_post(client):
    import requests

    response = json_request(client, '/matcher', {'matcher_input': 'ccccskjskgbg'})
    # url = "http://localhost:5000/matcher"
    # data = '{"matcher_input":"abcdefghijklmnopqrstuvwxyz"}'

    # response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.data == 'False'