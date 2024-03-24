#!/usr/bin/python3
"""
This module display "Python" followed by the value of the
text varaible
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Route /c/<text> returns C message
    only with varaible included
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
    Route /python/<text> returns Python message
    even without variable
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
