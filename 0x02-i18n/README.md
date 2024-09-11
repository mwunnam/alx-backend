# 0x02. i18n

## Flask-Babel
This is an extension for Flask that adds support for internationlization (i18n) and localization(l10n) in Flask application.
It provides features that translate the application into multiple languages and handle time zome coversions.
### Key Features
* Message Translation: Allows you mark certain text strings in the application for translation
* Locale Management: Automatically detects the user's language and set the appropriate locale.
* Date and Time Formatting: Helps to format date and time according to the user's locale.
* Plurals: Handles pluralization rules specific to different language
* Time Zone Support: Works with pytz to handle time zones in the applicatoin

## Basic Setup
1. Installation:
	`pip install Flask-Babel`

2. Configure Flask app, configure Babel:
```Python
	from flask import Flask
	from flask_babel import Babel

	app = Flask(__name__)
	app.config['BABEL_DEFAULT_LOCALE'] = 'en'
	app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

	babel = Babel(app)
```
3. Marking strings for Translation:
```Python
	from flask_babel import _

	@app.route('/')
	def home():
		return _("Hello, world!")
```

4. Creating Translation Files:
Use Babel's command-line tools to extract translatable strings and compile translation files:
```Bash
	pybabel extract -F babel.cfg -o message.pot .
	pybabel init -i messages.pot -d translations -l es
	pybabel compile -d translations
```




