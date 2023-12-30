#!/usr/bin/python3
"""
this file contains the url when http://0.0.0.0:5000/ or curl 0.0.0.0:5000
entered it will respond
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """this will be called when the above url entered

    Returns:
        str: this will return string value
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
