#!/usr/bin/python3
"""
Runs the web application and renders the different views
"""
from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the homepage"""
    return render_template('index.html')


if __name__ == '__main__':
    host = os.getenv('WEB_APP_HOST', '0.0.0.0')
    port = os.getenv('WEB_APP_PORT', 5000)
    app.run(host=host, port=port)
