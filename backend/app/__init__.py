from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging
from logging import Formatter, FileHandler
import babel
import dateutil.parser
import random

from .config import Config

app = Flask(__name__, '/api')
app.config.from_object(Config)
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from .blueprints import *

app.register_blueprint(core, url_prefix='/api')
app.register_blueprint(category, url_prefix='/api')
app.register_blueprint(question, url_prefix='/api')
app.register_blueprint(quiz, url_prefix='/api')

@app.before_first_request
def before_first_request_func():

    pass


@app.before_request
def before_request():

    pass


@app.after_request
def after_request(response):

    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')

    return response


@app.teardown_request
def teardown_request(error=None):

    db.session.close()

@app.errorhandler(404)
def not_found(error):
    '''
    Error handler for expected error 404.
    '''

    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found",
    }), 404

@app.errorhandler(405)
def not_found(error):
    '''
    Error handler for expected error 405.
    '''

    return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed",
    }), 405

@app.errorhandler(422)
def unprocessable(error):
    '''
    Error handler for expected error 422.
    '''

    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable",
    }), 422

@app.errorhandler(500)
def server_error(error):
    '''
    Error handler for expected error 500.
    '''

    return jsonify({
        "success": False,
        "error": 500,
        "message": "server error",
    }), 500
