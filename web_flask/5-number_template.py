#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displays Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return ('{} is a number'.format(n))


@app.route('/number/', strict_slashes=False)
@app.route('/number_template/<int:n>/', strict_slashes=False)
def num_temp(n):
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
