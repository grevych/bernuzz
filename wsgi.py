# -*- coding: utf-8 -*-
"""

"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from crm.apps import website, api


application = DispatcherMiddleware(
    website.create_app(),
    {'/api/1': api.create_app()})

if __name__ == "__main__":
    run_simple(
        '0.0.0.0',
        5000,
        application,
        use_reloader=True,
        use_debugger=True)
