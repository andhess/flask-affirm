# Flask Affirm
This project is for demo purposes only. It shows the Affirm Direct API integration in action against the Sandbox environment.

## Requirements
* Make sure Python 3 is installed
* You will need to install less via NPM

## Setup
You will need to add your Affirm Sandbox API keys in a couple locations:
1. Public and Private to `secret.py`
2. Public to `static/js/affirm.js`

You will also need to set a environment variable for the `FLASK_APP`. Just run this line in the project's root directory.

`$ export FLASK_APP=main.py`

## Running the application
The command below will start the Flask server

`python -m flask run`
