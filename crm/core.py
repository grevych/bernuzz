# -*- encoding:utf-8 -*-

#from flask_mail import Mail
# from flask_sqlalchemy import SQLAlchemy
# from flask_security import Security, SQLAlchemyUserDatastore

from flask import Flask
from mongoengine import connect

from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension

from helpers import register_blueprints
from middlewares import HTTPMethodOverrideMiddleware


#db = SQLAlchemy()
#mail = Mail()
#security = Security()
#social = Social()
db = MongoEngine()
toolbar = DebugToolbarExtension()


def create_app(
    package_name,
    package_path,
    settings_override=None,
    register_security_blueprint=True
):
    """Returns a :class:'Flask' application instance configured with common
    functionality.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_security_blueprint: flag to specify if the Flask-Security
                                       Blueprint should be registered. Defaults
                                       to `True`.
    """

    app = Flask(package_name, instance_relative_config=True)
    app.config.from_object('crm.settings.development')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)
    #app.config.from_envvar('FLASKR_SETTINGS', silent=True)

    db.init_app(app)
    toolbar.init_app(app)
    # db.init_app(app)
    # mail.init_app(app)
    # security.init_app(
    #     app,
    #     SQLAlchemyUserDatastore(db, User, Role),
    #     register_blueprint=register_security_blueprint)

    # @app.before_first_request
    # def before_first_request():
    #     try:
    #         import apps.models
    #         apps.models.db.create_all()
    #     except Exception, e:
    #         app.logger.error(str(e))

    # @app.context_processor
    # def template_extras():
    #     return dict(
    #         google_analytics_id=app.config.get('GOOGLE_ANALYTICS_ID', None))

    # @app.errorhandler(SocialLoginError)
    # def social_login_error(error):
    #     return redirect(
    #         url_for('website.register', provider_id=error.provider.id, login_failed=1))

    register_blueprints(app, package_name, package_path)
    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

    return app
