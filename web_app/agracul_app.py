#!/usr/bin/python3
"""
Runs the web application and renders the different views
"""
from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def welcome():
    """
    Routes to the welcome page
    """
    return render_template('index.html')

@app.route('/home', strict_slashes=False)
def home():
    """
    Routes to the home page
    """
    return render_template('home.html')

@app.route('/login', strict_slashes=False)
def login():
    """
    Routes to the login page
    """
    return render_template('login.html')

@app.route('/signup', strict_slashes=False)
def signup():
    """
    Routes to the signup page
    """
    return render_template('signup.html')


if __name__ == '__main__':
    host = os.getenv('WEB_APP_HOST', '0.0.0.0')
    port = os.getenv('WEB_APP_PORT', 5000)
    app.run(host=host, port=port)
