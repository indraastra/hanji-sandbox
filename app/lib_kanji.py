import os
import xmltodict

import flask


__ROOT_DIR__ = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(__ROOT_DIR__, '..', 'data', 'kanji')


filters = flask.Blueprint('filters', __name__)


def path_to_kanji(kanji):
    filename = "{:05x}.svg".format(ord(kanji[0]))
    return os.path.join(SVG_DIR, filename)

@filters.app_template_filter()
def load_xml(kanji):
    svg_file_name = path_to_kanji(kanji)
    with open(svg_file_name) as svg:
        return svg.read()

@filters.app_template_filter()
def parse_svg(raw_xml):
    xmld = xmltodict.parse(raw_xml)
    xmld['svg']['@width']  = '300'
    xmld['svg']['@height'] = '300'
    return xmld

@filters.app_template_filter()
def unparse_svg(xmld):
    xml = xmltodict.unparse(xmld)
    return xml
