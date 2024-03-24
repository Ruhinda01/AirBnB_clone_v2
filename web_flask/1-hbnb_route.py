#!/usr/bin/python3
"""web application that has "/" and "/hbnb" routes"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns "HBNB"
    """
    return "HBNB"
