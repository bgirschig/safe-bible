from book_tools import books, ordered_books, highlights, get_verse_text, get_verse_labels, get_chapter_labels, books_summary
from config import labelMap
import json
from os import path

# 'appData.json' is built dynamically to ensure the data is consistent between server and app
# (mostly for share-image generation)
# We pre-build it because the flask endpoint that was creating it was very slow (~4sec), even when
# preparing it as a string that was returned when requested.

# This script is called by the build-and-deploy script, after the frontend has been built

basepath = path.dirname(__file__)
with open(path.join(basepath, "static/appData.json"), "w+") as f:
  json.dump({
    "books": books_summary,
    "highlights": highlights,
    "labelMap": labelMap,
  }, f, separators=(',', ':'))