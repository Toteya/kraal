#!/usr/bin/python3
"""
Contains users API views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.user import User

@app_views.route('/users',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def users():
    """
    Return all users
    """
    if request.method == 'GET':
        users = storage.all(User).values()
        users_dicts = []
        for user in users:
            users_dicts.append(user.to_dict())
        return jsonify(users_dicts)
    if request.method == 'POST':
        data = request.get_json(silent=True)
        if not data:
            abort(400, 'Not a valid JSON')
        first_name = data.get('first_name')
        if first_name is None:
            abort(400, 'Missing: first_name')
        last_name = data.get('last_name')
        if last_name is None:
            abort(400, 'Missing: last_name')
        email = data.get('email')
        if email is None:
            abort(400, 'Missing: email')
        password = data.get('password')
        if password is None:
            abort(400, 'Missing: password')
        obj = User(**data)
        obj.save()
        return jsonify(obj.to_dict()), 201
    

# @app_views.route('/users')
# def user