#!/usr/bin/python3
"""
Contains generic API views
"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', strict_slashes=False)
def status():
    """
    Return current status of API
    """
    return jsonify({'status': 'OK'})