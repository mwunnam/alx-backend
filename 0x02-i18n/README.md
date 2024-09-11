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
the files will have the extesion .po for human readable translation files and .mo for machine readable files
`.po` Portable Object
`.mo` Machine Object
## Directory Structure:
```
/your_flask_app
|-- /translations
|   |-- /<language_code>
|   |   |-- /LC_MESSAGES
|   |   |   |-- messages.po
|   |   |   |-- messages.mo
|   |
|   |-- /es
|   |   |-- /LC_MESSAGES
|   |   |   |-- messages.po
|   |   |   |-- messages.mo
|   |
|   |-- /fr
|       |-- /LC_MESSAGES
|           |-- messages.po
|           |-- messages.mo
```
## Flask i18n
Internationalization in Flask is the process of designing web application so that it can adpt to various language and regions without engineering changes. Flask-Babel does this by managing translations and locale data
### Steps for Flask i18n:
1. Setup Flask-Babel
2. Extract Translatable Text
	* Use `pybabel exctract` to scan they python files for translatable strings marked with `_()` and generate a `.po` file for each language you want to support.
3. Create Translation files:
	Use `pybabel init` to create a `.po` file for each language you want to support.
4. Translate Strings:
	* Edit the `.po` file to provide translations for each language
5. Compile Translations:
	* Use `pybabel compile` to compile the `.po` file into binary `.mo` files that Flask-Babel can use
6. Handle Locale Switching
	* You can switch locales based on the user preference or browers setting by configuring the `@babel.localeselector` decorator

## Pytz

This is a Python libray that brings the Olson tz database into python, making it possible to get accurate and cross-platform time zone calculations. It helps in the the conversion of time and dates between different zones. This is very important for handling time related data globally.
### Key Features:
	* Time zone conversions: Converts native datetime objects to aware datetime objects in any time zone
	* Daylight Saving Time: Handles daylight saving time transitions properly
	* Wide Range of Time Zones: Supports all time zones defined by the Olson database.

### Basic Usage:
	1. Installation: `pip install pytz`
	2. Basic program
		```Python
		import pytz
		from datatime import datatime

		# Getting the current time in UTC
		utc_time = datatime.utcnow()

		# Converting UTC time to a specific timezone
 		tz = pytz.timezone('America/New_York')
 		local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(tz)
 		print(f'UTC time: {utc_time}')
 		print(f'Local time: {local_time}')

		# List all time Zones
		for tz in pytz.all_timezones:
			print(tz)
		```
