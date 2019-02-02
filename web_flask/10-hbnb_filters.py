#!/usr/bin/python3
"""starts a Flask web application"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.lstrip_blocks = True
app.jinja_env.rstrip_blocks = True


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    return render_template('10-hbnb_filters.html',
                           state=storage.all('State'),
                           amenity=storage.all('Amenity'))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
