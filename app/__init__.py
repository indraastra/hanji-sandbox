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
    app.register_blueprint(browse)  # Registers at / (root).
    app.register_blueprint(filters)

    # TODO: Add to config.py that ISN'T in git.
    app.secret_key = b'\x06\xf1\xe4\x18y\x10\xd1\xbf\x1e\xf9\xa6\xbe\x862>\xb3+\xa1\x7f\x07\xe761\xbd'

    return app


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app = create_app()
    app.run(debug=True)
