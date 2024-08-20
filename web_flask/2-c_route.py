#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route('hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Replace underscores with spaces"""
    return f"C {text.replace('_', ' ')}"


if __name__ = "__main__":
    app.run(host="0.0.0.0", port=5000)
