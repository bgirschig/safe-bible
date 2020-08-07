from flask import Flask, render_template, jsonify, request, send_file
from book_tools import books, ordered_books, highlights, get_verse_text, get_verse_labels, get_chapter_labels
import json
import shareImage
import itertools
from random import randint
from config import labelMap

app = Flask(__name__, static_folder="static", static_url_path='/')

# this is a trick to catch every route that didn't match anything here
# or in the assets folder. It is necessary for vue's 'history mode'
@app.errorhandler(404)
@app.route("/")
def home(err=None):
  return render_template("index.html",
    sharing="plb",
  )

# Todo: do this once and put it in memory
@app.route("/books")
def booksHandler():
  bookCount = len(ordered_books)
  data = [{
    "id": book["id"],
    "prev": ordered_books[bookIdx-1]["id"] if bookIdx > 0 else None,
    "next": ordered_books[bookIdx+1]["id"] if bookIdx < bookCount-1 else None,
    "bibleHubId": book["bibleHubId"],
    "short": book["short"],
    "full": book["full"],
    "group": book["group"],
    "chapterCount": len(book["chapters"])
  } for bookIdx, book in enumerate(ordered_books)]
  return jsonify({
    "books": data,
    "highlights": highlights,
  })

@app.route("/chapter/<string:bookId>/<int:chapterIdx>")
def chapterHandler(bookId, chapterIdx):
  chapterIdx -= 1
  if not bookId or bookId not in books:
    return jsonify({"error": 'BOOK_NOT_FOUND'}), 404
  if chapterIdx < 0 or chapterIdx >= len(books[bookId]["chapters"]):
    return jsonify({"error": 'CHAPTER_NOT_FOUND'}), 404
  
  return jsonify(books[bookId]["chapters"][chapterIdx])

@app.route('/shareImage/<bookId>/<int:chapter>/<int:verse>')
def getVerseImage(bookId, chapter, verse):
  verseData = books[bookId]["chapters"][chapter-1][verse-1]

  labels = [labelMap[key] for key in get_verse_labels(verseData)]
  text = get_verse_text(verseData)
  bookName = books[bookId]["short"]

  img = None
  if (labels):
    img = shareImage.makeVerseImage(text, f"{bookName} {chapter}:{verse}", labels)
  else:
    img = f"shareImage/static/share_{randint(1,6)}.jpg"

  return send_file(img, mimetype='image/png')

@app.route('/shareImage/<bookId>/<int:chapter>')
def getChapterImage(bookId, chapter=1):
  chapterData = books[bookId]["chapters"][chapter-1]
  labels = [labelMap[key] for key in get_chapter_labels(chapterData)]
  title = books[bookId]["multiline"] if "multiline" in books[bookId] else books[bookId]["full"]
  img = shareImage.makeChapterImage(title, labels, chapter)
  return send_file(img, mimetype='image/png'), 200

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)