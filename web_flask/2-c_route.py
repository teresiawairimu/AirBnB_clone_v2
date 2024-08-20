#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route to display Hello HBNB!"""
    return "Hello HBNB!"


@app.route('hbnb', strict_slashes=False)
def hbnb():
    """Route to displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route to display C followed by the value of the text
       Replace underscores with spaces

       Args:
           text (str): The text to display after C
       Returns:
           str: The formatted string with C followed the text.

    """
    return f"C {text.replace('_', ' ')}"


if __name__ = "__main__":
    app.run(host="0.0.0.0", port=5000)
