import os
import logging

from flask import Flask
from flask import redirect, request, send_from_directory, url_for


app = Flask(__name__)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(ROOT_DIR, '..', 'data', 'kanji')


def kanji_to_filename(kanji):
    return "{:05x}.svg".format(ord(kanji[0]))


@app.route('/')
def index():
    return redirect(url_for('lookup', kanji='我'))


@app.route('/svg/<filename>')
def raw_svg(filename):
    logging.info("Reading file {}".format(filename))
    return send_from_directory(SVG_DIR, filename)


@app.route('/lookup/<kanji>')
def lookup(kanji):
    filename = kanji_to_filename(kanji)
    logging.info("Reading file {}".format(os.path.join(SVG_DIR, filename)))
    return send_from_directory(SVG_DIR, filename)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)
