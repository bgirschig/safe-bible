from flask import Flask, render_template, jsonify, request, send_file
from book_tools import books, ordered_books, highlights, get_verse_text, get_verse_labels, get_chapter_labels, books_summary
from werkzeug.security import generate_password_hash, check_password_hash
import json
import shareImage
import itertools
from random import randint
from config import labelMap, sharingDefaults, baseUrl
from flask_httpauth import HTTPBasicAuth

DAYS = 60*60*24

app = Flask(__name__, static_folder="static", static_url_path='/')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 365*DAYS
auth = HTTPBasicAuth()

users = {
  "bgirschig": generate_password_hash("L%mWn<JaV*QSL4-:"),
  "jMeter": generate_password_hash(")6{iM@s>'-4zu#q"),
  "caro-lyn": generate_password_hash("butter"),
}

@auth.verify_password
def verify_password(username, password):
  return username
  if username in users and \
    check_password_hash(users.get(username), password):
    return username

# this is a trick to catch every route that didn't match anything here
# or in the assets folder. It is necessary for vue's 'history mode'
@app.errorhandler(404)
@app.route("/")
@auth.login_required
def home(err=None):
  return render_template("index.html",
    description=sharingDefaults["description"],
    sharing=get_sharing_for_current_route(),
    sharedVerse=json.dumps(getVerse(request.args.get('verse'))),
  )

def get_sharing_for_current_route():
  sharing = dict(sharingDefaults)

  sharing["url"] = f"{baseUrl}"
  sharing["image"] = f"{baseUrl}/shareImage"

  verseId = request.args.get("verse")
  chapterId = request.args.get("chapter")
  if verseId:
    sharing["image"] = f"{baseUrl}/shareImage/{verseId}"
    sharing["url"] = f"{baseUrl}?verse={verseId}"
  elif chapterId:
    sharing["image"] = f"{baseUrl}/shareImage/{chapterId}"
    sharing["url"] = f"{baseUrl}?verse={chapterId}"
  else:
    address = parsePath(request.path)
    if (address["bookId"] and address["bookId"] in books and len(books[address["bookId"]]["chapters"]) > 0 ):
      sharing["image"] = f"{baseUrl}/shareImage/{address['bookId']}/{address['chapterIdx']+1}"
      sharing["url"] = f"{baseUrl}?chapter={address['bookId']}/{address['chapterIdx']+1}"
  return sharing

def parsePath(path):
  parts = path.strip("/").split("/")
  return {
    "bookId": parts[0] or None,
    "chapterIdx": int(parts[1])-1 if len(parts)>1 else 0,
    "verseIdx": int(parts[2])-1 if len(parts)>2 else None,
  }

@app.route("/books/")
@app.route("/books")
def booksHandler():
  print(books_summary)
  return jsonify({
    "books": books_summary,
    "highlights": highlights,
    "labelMap": labelMap,
  })

@app.route("/chapter/<string:bookId>/<int:chapterIdx>/")
@app.route("/chapter/<string:bookId>/<int:chapterIdx>")
def chapterHandler(bookId, chapterIdx):
  chapterIdx -= 1
  if not bookId or bookId not in books:
    return jsonify({"error": 'BOOK_NOT_FOUND'}), 404
  if chapterIdx < 0 or chapterIdx >= len(books[bookId]["chapters"]):
    return jsonify({"error": 'CHAPTER_NOT_FOUND'}), 404
  
  return jsonify(books[bookId]["chapters"][chapterIdx])

def getVerse(verseId):
  if not verseId: return None

  address = parsePath(verseId)
  bookId = address['bookId']
  chapterIdx = address['chapterIdx']
  verseIdx = address['verseIdx']

  if not bookId or bookId not in books:
    return jsonify({"error": 'BOOK_NOT_FOUND'}), 404
  if chapterIdx < 0 or chapterIdx >= len(books[bookId]["chapters"]):
    return jsonify({"error": 'CHAPTER_NOT_FOUND'}), 404
  if verseIdx < 0 or verseIdx >= len(books[bookId]["chapters"][chapterIdx]):
    return jsonify({"error": 'CHAPTER_NOT_FOUND'}), 404

  verse = dict(books[bookId]["chapters"][chapterIdx][verseIdx])
  verse["title"] = f"{books[bookId]['short']} {chapterIdx+1}:{verseIdx+1}"
  verse["labels"] = list(get_verse_labels(verse))
  verse["text"] = get_verse_text(verse)

  return verse

@app.route('/shareImage/<bookId>/<int:chapter>/<int:verse>/')
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

@app.route('/shareImage/<bookId>/')
@app.route('/shareImage/<bookId>')
@app.route('/shareImage/<bookId>/<int:chapter>/')
@app.route('/shareImage/<bookId>/<int:chapter>')
def getChapterImage(bookId, chapter=1):
  chapterData = books[bookId]["chapters"][chapter-1]
  labels = [labelMap[key] for key in get_chapter_labels(chapterData)]
  title = books[bookId]["multiline"] if "multiline" in books[bookId] else books[bookId]["full"]
  img = shareImage.makeChapterImage(title, labels, chapter)
  return send_file(img, mimetype='image/png'), 200

@app.route('/shareImage/')
@app.route('/shareImage')
def getStaticShareImage():
  return send_file(
    f"shareImage/static/share_{randint(1,6)}.jpg",
    mimetype='image/png'
  )

# @app.after_request
# def add_header(response):
#   print(request.path)
#   response.cache_control.max_age = 3*DAYS
#   return response

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
