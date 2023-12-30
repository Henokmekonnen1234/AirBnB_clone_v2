#!/usr/bin/python3
"""
this file contains the url when http://0.0.0.0:5000/ or curl 0.0.0.0:5000
entered it will respond
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """this will be called when the above url entered

    Returns:
        str: this will return string value
    """
    return "{}".format("Hello HBNB!")


@app.route("/hbnb")
def hbnb():
    """this will be called when http://0.0.0.0:5000/hbnb or
       curl 0.0.0.0:5000/hbnb url entered

    Returns:
        str: this will return string value
    """
    return "{}".format("HBNB")


@app.route("/c/<text>")
def clang(text):
    """this will be called when http://0.0.0.0:5000/c/<text> or
       curl 0.0.0.0:5000/c/<text> url entered

    Attrib:
        text (any): str value sent by url

    Returns:
        str: this will return string value
    """
    text = escape(text)
    if "_" in text:
        text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", defaults={"text": "is cool"})
def pthon(text):
    """this will be called when http://0.0.0.0:5000/python/<text> or
       curl 0.0.0.0:5000/python/<text> url entered

    Attrib:
        text (any): str value sent by url

    Returns:
        str: this will return string value
    """
    text = escape(text)
    if "_" in text:
        text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
