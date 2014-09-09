# -*- coding: utf-8 -*-
"""

"""

import sys

from threading import Lock
from werkzeug.exceptions import NotFound

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from .apps import website, api


class SubdomainDispatcher(object):

    def __init__(self, domain, create_app):
        self.domain = domain
        self.create_app = create_app
        self.lock = Lock()
        self.instances = {}

    def get_application(self, host):
        host = host.split(':')[0]
        assert host.endswith(self.domain), 'Configuration error'
        subdomain = host[:-len(self.domain)].rstrip('.')
        with self.lock:
            app = self.instances.get(subdomain)
            if app is None:
                app = self.create_app(subdomain)
                self.instances[subdomain] = app
            return app

    def __call__(self, environ, start_response):
        app = self.get_application(environ['HTTP_HOST'])
        return app(environ, start_response)


def make_app(subdomain):
    apps = {
        '': website.create_app,
        'api': api.create_app
    }

    if not subdomain in apps:
        return NotFound()

    if hasattr(apps[subdomain], '__call__'):
        return apps[subdomain]()

    return DispatcherMiddleware(*apps[subdomain])


domain = sys.argv[1] if len(sys.argv) > 1 else "localhost"
application = SubdomainDispatcher(domain, make_app)

if __name__ == "__main__":
    run_simple(
        '0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
