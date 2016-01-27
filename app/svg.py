import os

from flask import current_app, Blueprint, redirect, render_template,\
                  send_from_directory, url_for

import app.lib_kanji as libk


svg = Blueprint('admin', __name__)


@svg.route('/')
def index():
    return redirect(url_for('.svg_kanji_raw', kanji='我'))


@svg.route('/static/<filename>')
def svg_static(filename):
    current_app.logger.info("Loading file {}".format(filename))
    return send_from_directory(libk.SVG_DIR, filename)


@svg.route('/raw/<kanji>')
def svg_kanji_raw(kanji):
    filename = libk.kanji_to_filename(kanji)
    current_app.logger.info("Loading file {}".format(os.path.join(SVG_DIR, filename)))
    return send_from_directory(libk.SVG_DIR, filename)


@svg.route('/pretty/<kanji>')
def svg_kanji_pretty(kanji):
    filename = libk.kanji_to_filename(kanji)
    current_app.logger.info("Loading file {}".format(os.path.join(SVG_DIR, filename)))
    return send_from_directory(libk.SVG_DIR, filename)
