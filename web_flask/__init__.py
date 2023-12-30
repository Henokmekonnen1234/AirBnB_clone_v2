#!/usr/bin/python3
"""
this will initializes the app and will be available for all
files in this module
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes=False
