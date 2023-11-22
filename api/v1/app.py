#!/usr/bin/python3
"""
Runs the web application API
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def close_session(error=None):
    """
    Closes the database session
    """
    storage.close()

@app.errorhandler(404)
def not_found(error=None):
    """"
    Returns 404 Error - for API resource not found
    """
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    """Run the application"""
    host = os.getenv('KRAAL_API_HOST', '0.0.0.0')
    port = os.getenv('KRAAL_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)