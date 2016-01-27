import os
import logging

from flask import Flask
from flask import redirect, request, send_from_directory, url_for
from flask.ext.bootstrap import Bootstrap


def create_app():
    from .svg import svg
    from .browse import browse
    from .lib_kanji import filters

    app = Flask(__name__)
    Bootstrap(app)

    app.register_blueprint(svg, url_prefix='/svg')
    app.register_blueprint(browse, url_prefix='/')
    app.register_blueprint(filters)
    return app


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app = create_app()
    app.run(debug=True)
