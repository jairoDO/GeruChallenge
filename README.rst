quotes README
==================

Getting Started
---------------

- cd quotes

- $VENV/bin/pip install -e .

- $VENV/bin/initialize_quotes_db development.ini

- $VENV/bin/pserve development.ini



## Challenge

### 1) Create a lib that will act as a wrapper around the API described above

For resolve this item, I have created the package quote_lib, I decided store into this repository because it is a little project.
but it is possible separate this project.

### 2) Create a Pyramid [1] application that will use the API

The application must have 4 routes:

 * `/` - Presents a simple HTML page containing a title that reads "Web Challenge 1.0".
 * `/quotes` - Presents a page containing all quotes returned by the API (each contained in its own bullet point).
 * `/quotes/<quote_number>` - Presents a page containing the `<quote_number>` quote returned by the API.
 * `/quotes/random` - Present a page containing a random quote. Both the `<quote_number>` and the quote selected randomly ought to be displayed.

[1] https://docs.pylonsproject.org/projects/pyramid/en/latest/

* For resolve this item I have used the library made in the before items. and I create 4 views
* '/' - This route is implemented by function home inside in views/default.py
* '/quotes' - This route is implemented by function 'quotes' inside views/quotes.py
* '/quotes/<quote_number>' - This route is implemented by function 'get_quote_view' inside of views/quotes.py
* `/quotes/random` - This route is implemented by function 'random_view' inside of views/quotes.py

### 3) Create and register the session

Using the framework's session mechanism, create a unique identifier for all application requests that came from the same browser.


### 4) Store requests in a database

Using `SQLAlchemy` + `sqlite` create a model (or models) to store:
* The session identifier
* The date, time and page requested within a given session for every request made.
* In quotes/models/mymodels.py I have crated a class SessionModel and I decided resolve this item subscribing the event BeforeRender in quotes/quotes/__init__.py


### 5) Create RESTful endpoints to query the sessions/requests stored in the database

* Here there was two options the first one it was use a library like as ramses, but I think that was too much for the simple think then I decided create to new view (function requests inside of /views/quotes/ ) and add Method to_json to SessionModel.
