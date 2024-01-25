#!/usr/bin/python3
"""
This module contain Flask web application.
It will list State information like
state id and name from database using the url
curl 0.0.0.0:5000/states_list
"""

from flask import Flask, abort, render_template
from logging import error
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def state_list():
    """ this method will show the list of states
    """
    try:
        state = {}
        storage.close()
        for _, value in storage.all(State).items():
            state[value.id] = value.name
        return render_template("7-states_list.html", state=state)
    except Exception as e:
        error("Error occurred", e)


@app.teardown_appcontext
def teardown(error=None):
    """used to register a function that will be called when
        the application context ends.
    """
    try:
        storage.close()
    except Exception as e:
        error("Error occurred {}".format(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
