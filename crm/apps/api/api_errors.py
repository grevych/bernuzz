# encoding: utf-8
"""
errors.py

Created by grevych on 2014-07-25.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

from flask import jsonify

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
        
        
# @app.errorhandler(InvalidUsage)
# def handle_invalid_usage(error):
#     response = jsonify(error.to_dict())
#     response.status_code = error.status_code
#     return response
#     
#     
# @app.route('/foo')
# def get_foo():
#     raise InvalidUsage('This view is gone', status_code=410)