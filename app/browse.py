import os

from flask import current_app, Blueprint, redirect, render_template,\
                  send_from_directory, url_for

import app.lib_kanji as libk


browse = Blueprint('browse', __name__)


@browse.route('/')
def index():
    return render_template("index.html")
