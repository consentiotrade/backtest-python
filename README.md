# Test

## What we have, what to do

We have a rudimentary web server to upload and review stocks.
We would like to:

* Add clients and client portfolios: e.g. "Joe has: 34 shares of AAPL, 43 of MSFT ..."
* Create a current-value calculator for users: e.g. "Joe's portfolio is worth 234.25 EUR"
* Design (talk about, not code) a bulk uploader for user portfolios
* Design (talk about, not code) API for portfolio upload, portfolio viewing etc.
* Comment on code (your own or the existing code), positive and negative aspects
* Defend choices/design in the previous points
* What would you do next with this project?

## How to

* Install [pip](https://pip.pypa.io/en/stable/installing/)
* Install the project dependencies: `$ pip install -r requirements.txt`
* The following commands must be executed inside the `src` folder!!
* Run the server: `$ python main.py`
* The server is running on `http://0.0.0.0:8080`
* Run the tests: `$ python -m unittest discover -s tests`
