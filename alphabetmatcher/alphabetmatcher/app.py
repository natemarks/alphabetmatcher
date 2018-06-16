"""
This is the entry point for the alphabetmatcher application.

Main uses Flask to create a REST listener interface.  Data provided via POST is passed to alphabetmatcher.Matcher at
init. The output of Matcher.success() is returned via the POST response.

The application can be manually tested by running app.py then running the command below on the same host.

curl -i -X POST -H "Content-Type:application/json"  \
http://localhost:5000/matcher -d '{"matcher_input":"abcdefghijklmnopqrstuvwxyz"}'

This should produce a successsful test wiht the string "True"  like this:

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 4
Server: Werkzeug/0.14.1 Python/2.7.15
Date: Sat, 16 Jun 2018 00:20:03 GMT

True
"""

import json

from flask import Flask, request
from alphabetmatcher import Matcher

app = Flask(__name__)


@app.route("/matcher", methods=["POST"])
def get_matcher():
    request_body = json.loads(request.data)
    matcher_input = request_body["matcher_input"]
    this_matcher = Matcher(matcher_input)
    return str(this_matcher.success())

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
