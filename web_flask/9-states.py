#!/usr/bin/python3
"""starts a Flask web application"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.lstrip_blocks = True


@app.route('/states_list', strict_slashes=False)
def all_states():
    return render_template('7-states_list.html', storage=storage.all('State'))


@app.route('/cities_by_states', strict_slashes=False)
def all_cities():
    return render_template('8-cities_by_states.html',
                           storage=storage.all('State'))


@app.route('/states', strict_slashes=False)
def a_states():
    return render_template('7-states_list.html', storage=storage.all('State'))


@app.route('/states/<id>', strict_slashes=False)
def a_states_id(id):
    state_id = None
    for s_id in storage.all('State').values():
        if s_id.id == id:
            state_id = s_id
    return render_template('9-states.html',
                           state_id=state_id,
                           storage=storage.all('State'))


@app.teardown_appcontext
def teardown(error):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
