#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask
from flask import render_template
from flask import request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Languge Configurations Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    SECRET_KEY = "Nothingfornow"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determins the match with the supported languages"""
    accepted_languages = request.accept_languages

    return best_match or 'en'


@app.route('/')
def welcome():
    """Welcome"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
