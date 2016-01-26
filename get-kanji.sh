#!/bin/bash

# Thanks to:
# https://github.com/hardmaru/sketch-rnn/blob/master/get_kanji.sh
#fetch and unpack the data
mkdir data
cd data
wget https://github.com/KanjiVG/kanjivg/releases/download/r20150615-2/kanjivg-20150615-2-all.zip
unzip kanjivg-20150615-2-all.zip
