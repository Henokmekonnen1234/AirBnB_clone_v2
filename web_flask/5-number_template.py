#!/usr/bin/python3
"""
this file contains the url when http://0.0.0.0:5000/ or curl 0.0.0.0:5000
entered it will respond
"""

from flask import Flask, abort, render_template
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


@app.route("/python/<text>")
@app.route("/python/")
def pthon(text="is cool"):
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


@app.route("/number/<n>")
def isNum(n):
    """this will be called when http://0.0.0.0:5000/number/<n> or
       curl 0.0.0.0:5000/number/<n> url entered

    Attrib:
        n (any): value sent by url

    Returns:
        str: this will return string value

    Raises:
        abort(404): this will abourt if any exception occurred and it
                    will show 404 page(not found)
    """
    try:
        n = int(n)
        return "{} is a number".format(n)
    except Exception as e:
        abort(404)


@app.route("/number_template/<n>")
def num_template(n):
    """this will be called when http://0.0.0.0:5000/number_template/<n> or
       curl 0.0.0.0:5000/number_template/<n> url entered

    Attrib:
        n (any): value sent by url

    Returns:
        str: this will return string value

    Raises:
        abort(404): this will abourt if any exception occurred and it
                    will show 404 page(not found)
    """
    try:
        n = int(n)
        return render_template("5-number.html", n=n)
    except Exception as e:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
