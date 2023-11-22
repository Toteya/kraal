#!/usr/bin/python3
"""
Contains users API views
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User

@app_views.route('/users', strict_slashes=False)
def users():
    """
    Return all users
    """
    users = storage.all(User).values()
    users_dicts = []
    for user in users:
        users_dicts.append(user.to_dict())
    return jsonify(users_dicts)

# @app_views.route('users/')