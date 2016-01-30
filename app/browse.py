import os

from flask import current_app, Blueprint, flash, redirect, render_template,\
                  send_from_directory, url_for

import app.lib_kanji as libk


browse = Blueprint('browse', __name__)


@browse.route('/')
@browse.route('/index')
def index():
    return render_template("index.html")


@browse.route('/show/<kanji>')
def show_kanji(kanji):
    data = libk.parse_svg(libk.load_svg(kanji))
    if not data:
        flash("Character [{}] not found.".format(kanji))
        return render_template("show.html", kanji=kanji)
    original_svg = libk.unparse_svg(data)
    strokes = libk.extract_strokes(data)
    stroke_svgs = [render_template("strokes.svg", strokes=strokes[:i])
                   for i in range(1, len(strokes)+1)]
    print(stroke_svgs[0])

    return render_template("show.html",
                           kanji=kanji,
                           original_svg=original_svg,
                           stroke_svgs=stroke_svgs)
