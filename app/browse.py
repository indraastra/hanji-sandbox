import os

from flask import current_app, Blueprint, flash, redirect, render_template,\
                  send_from_directory, url_for

import app.lib_kanji as libk


browse = Blueprint('browse', __name__)


@browse.route('/')
@browse.route('/index')
def index():
    return render_template("index.html")


@browse.route('/show')
@browse.route('/show/<kanji>')
def show_kanji(kanji='我'):
    data = libk.parse_svg(libk.load_svg(kanji))
    if not data:
        flash("Character [{}] not found.".format(kanji))
        return render_template("show.html", kanji=kanji)
    strokes = libk.extract_strokes(data)
    original_svg = render_template("svg/character.svg", strokes=strokes)
    stroke_svgs = [render_template("svg/strokes.svg", strokes=strokes[:i])
                   for i in range(1, len(strokes)+1)]

    return render_template("show.html",
                           kanji=kanji,
                           original_svg=original_svg,
                           stroke_svgs=stroke_svgs)

@browse.route('/worksheet')
@browse.route('/worksheet/<int:cell_count>')
def worksheet(cell_count=25):
    cell = render_template("svg/gridcell.svg")
    return render_template("worksheet.html", cell_svg=cell, cell_count=cell_count)
