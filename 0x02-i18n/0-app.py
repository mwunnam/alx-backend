#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def welcome():
    """Welcome"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
