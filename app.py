import os, datetime, urlparse, re

from pymongo import Connection
from flask import Flask, request, Response, render_template

EMAIL_REGEX = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    if email and re.match(EMAIL_REGEX, email):
        signup = {
                'email': email,
                'ip': request.remote_addr,
                'time': datetime.datetime.utcnow(),
                }
        database.signups.insert(signup)
        return Response(status=201)
    else:
        return Response(status=400)

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
