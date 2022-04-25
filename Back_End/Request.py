import imp
import os
from storehandler import *
from flask import Flask, send_from_directory
from flask.helpers import safe_join

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('../Front_End', "index.html")
@app.route('/data')
def data():
    #Get last minute data
    newest = GetLastamp()
    return newest
if __name__ == '__main__':
    app.run()