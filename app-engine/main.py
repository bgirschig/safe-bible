from flask import Flask, render_template, jsonify, request
from book_tools import books, ordered_books, highlights
import json

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



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
