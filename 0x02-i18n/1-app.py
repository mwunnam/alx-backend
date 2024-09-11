#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Languge Configurations Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def welcome():
    """Welcome""" return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
