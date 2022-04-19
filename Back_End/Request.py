import os
from flask import Flask, send_from_directory
from flask.helpers import safe_join

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('../Front_End', "index.html")
if __name__ == '__main__':
    app.run()