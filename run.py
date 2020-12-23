####################################
# In this, we use Flask to start   #
# a web server.                    #
####################################

from flask import Flask
from threading import Thread

# Flask constructor takes the name of
# current module (__name__) as argument.

app = Flask('')

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
