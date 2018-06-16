"""
rest API interface for alphabetmatcher
"""

import datetime
import json
import time

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
