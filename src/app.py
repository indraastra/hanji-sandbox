from flask import Flask, request, send_from_directory

app = Flask(__name__)

def kanji_to_filename(kanji):
    return "{:05x}.svg".format(ord(kanji[0]))

@app.route('/svg/<codepoint>')
def raw_svg(codepoint):
    return send_from_directory('../data/kanji',
                               codepoint)

@app.route('/lookup/<kanji>')
def lookup(kanji):
    return send_from_directory('../data/kanji',
                               kanji_to_filename(kanji))


if __name__ == '__main__':
    app.run(debug=True)
