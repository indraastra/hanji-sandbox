import os
import xmltodict

import flask


__ROOT_DIR__ = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(__ROOT_DIR__, '..', 'data', 'kanji')


filters = flask.Blueprint('filters', __name__)


def path_to_kanji(kanji):
    filename = "{:05x}.svg".format(ord(kanji[0]))
    path = os.path.join(SVG_DIR, filename)
    if os.path.exists(path):
        return path


def load_svg(kanji):
    svg_file_name = path_to_kanji(kanji)
    if not svg_file_name: return
    with open(svg_file_name) as svg:
        return svg.read()


def parse_svg(svg):
    if not svg: return
    svgd = xmltodict.parse(svg)
    return svgd


@filters.app_template_filter()
def unparse_svg(svgd):
    print(svgd)
    svg = xmltodict.unparse(svgd)
    return svg


@filters.app_template_filter()
def kanji_to_svg(kanji):
    svg = load_svg(kanji)
    if not svg: return
    svgd = parse_svg(svg)
    if not svgd: return
    svgd['svg']['@width']  = '300'
    svgd['svg']['@height'] = '300'
    return unparse_svg(svgd)


def extract_strokes(svgd):
    svg = svgd['svg']
    g = svg['g']
    assert(len(g) == 2)
    strokes = []
    def _extract_strokes(svgd):
        for k, v in svgd.items():
            if k == 'path':
                strokes.append({k: v})
            elif isinstance(v, xmltodict.OrderedDict):
                _extract_strokes(v)
            elif isinstance(v, list):
                for s_v in v:
                    _extract_strokes(s_v)
    _extract_strokes(svgd)
    return strokes


