# -*- coding: utf-8 -*-


from functools import wraps

from flask import render_template
from flask_security import LoginForm
from flask_security import  current_user, login_required, login_user

from crm import core
#from . import assets

app = None

def create_app(settings_override=None):
    """Returns the Overholt dashboard application instance"""
    global app
    app = core.create_app(__name__, __path__, settings_override)

    # Init assets
    #assets.init_app(app)
    
    # print dir(core.security)

    # Register custom error handlers
    if not app.debug:
        for e in [500, 404]:
            app.errorhandler(e)(handle_error)

    return app


def handle_error(e):
    return render_template('errors/%s.html' % e), e


def route(bp, *args, **kwargs):
    def decorator(f):
        @bp.route(*args, **kwargs)
        @login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return f

    return decorator