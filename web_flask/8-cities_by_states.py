#!/usr/bin/python3
"""starts a Flask web application"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def all_states():
    return render_template('7-states_list.html', storage=storage.all('State'))


@app.route('/cities_by_states', strict_slashes=False)
def all_cities():
    return render_template('8-cities_by_states.html',
                           storage=storage.all('State'))


@app.teardown_appcontext
def teardown(error):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
