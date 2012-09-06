import os
import datetime
import urlparse
import re

from pymongo import Connection
from flask import Flask, render_template, request

EMAIL_REGEX = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    if re.match(EMAIL_REGEX, email):
        signup = {
                'email': email,
                'date': datetime.datetime.utcnow(),
                }
        database.signups.insert(signup)
        return "Thanks! You'll hear from us soon."
    else:
        return "Err... we need a valid email address."

def connect_to_db():
    """Connect to database"""
    global database

    MONGOLAB_URI = os.environ['MONGOLAB_URI']
    MONGODB_HOST = urlparse.urlparse(MONGOLAB_URI).geturl()
    MONGODB_PORT = urlparse.urlparse(MONGOLAB_URI).port
    DATABASE_NAME = urlparse.urlparse(MONGOLAB_URI).path[1:]

    connection = Connection(MONGODB_HOST, MONGODB_PORT)
    database = connection[DATABASE_NAME]

if __name__ == '__main__':
    connect_to_db()
    port = int(os.environ.get('PORT', 5000))
    if port == 5000:
        app.debug = True
    app.run(host='0.0.0.0', port=port)
