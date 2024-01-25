#!/usr/bin/python3
"""
module
This module will dispaly city and states lists in the html page
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def citiesState():
    """This method will return the value of states with their respectve  cities
    Returns:
        render_template():  returns the rendered HTML content.
    """
    try:
        state = [value for _, value in storage.all(State).items()]
        return render_template("8-cities_by_states.html", state=state)
    except Exception as e:
        print("Error occured", e)


@app.teardown_appcontext
def teardown(error=None):
    """This method is used to remove the current session
    """
    try:
        storage.close()
    except Exception as e:
        print("Error Occured")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
