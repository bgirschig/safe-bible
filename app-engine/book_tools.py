import json
import csv
from config import CENSOR_TRESHOLD, labelMap

books = {}
highlights = {}
books_summary = []

# load book titles
with open("./data/books.json") as f:
  ordered_books = json.load(f)

def init():
  for book_idx, book in enumerate(ordered_books):
    book["idx"] = book_idx
    book["chapters"] = []
    books[book["id"]] = book

  # load sentence data
  with open("./data/sentences.csv") as f:
    reader = csv.DictReader(f)
    prevPosition = None
    for row in reader:
      position = row["position"]

      # Some verses contain multiple sentences. This helps us determine wether the current
      # sentence is the first one in the verse, so that we can hide the verse number/link for
      # the other ones
      is_new_verse = prevPosition != position
      prevPosition = position

      position = json.loads(position)
      if len(position) != 3: continue
      bookId, chapter, verseIdx = position

      chapter -= 1
      verseIdx -= 1

      if (bookId not in books): raise f"unexpected book id: {bookId}"
      
      chapters = books[bookId]["chapters"]
      while (chapter >= len(chapters) ): chapters.append([])
      labels = [key for key in labelMap if float(row[key]) > CENSOR_TRESHOLD]
      sentence = {
        "text": row["text"],
        "labels": labels,
      }

      while verseIdx >= len(chapters[chapter]):
        tmpVerseIdx = len(chapters[chapter])+1
        chapters[chapter].append({
          "verseIdx": tmpVerseIdx,
          "verseId": f"{bookId}/{chapter+1}/{tmpVerseIdx}",
          "bibleHubLink": f"https://biblehub.com/{books[bookId]['bibleHubId']}/{chapter+1}-{position[2]}.htm",
          "sentences": []
        })
      chapters[chapter][verseIdx]["sentences"].append(sentence)

  # create a 'book map'
  global books_summary
  bookCount = len(ordered_books)
  books_summary = [{
    "id": book["id"],
    "prev": ordered_books[bookIdx-1]["id"] if bookIdx > 0 else None,
    "next": ordered_books[bookIdx+1]["id"] if bookIdx < bookCount-1 else None,
    "bibleHubId": book["bibleHubId"],
    "short": book["short"],
    "full": book["full"],
    "group": book["group"],
    "chapterCount": len(book["chapters"])
  } for bookIdx, book in enumerate(ordered_books)]

  # load highlights
  global highlights
  with open("./data/highlights.json") as f:
    highlight_addresses = json.load(f)
    for address in highlight_addresses:
      bookId, chapterIdx, verse = address
      if bookId not in highlights:
        highlights[bookId] = {
          "bookTitle": books[bookId]["full"],
          "chapters": {}
        }
      if chapterIdx not in highlights[bookId]["chapters"]:
        highlights[bookId]["chapters"][chapterIdx] = []
      highlights[bookId]["chapters"][chapterIdx].append(books[bookId]["chapters"][chapterIdx-1][verse-1])

  highlights = [highlights[book["id"]] for book in ordered_books if book["id"] in highlights]
    
def get_nav_links(bookId:str, chapter:int):
  """ Returns tuple with prev and next page links for a given page ID (bookId+chapterId)"""

  current_book = books[bookId]

  prevPage = current_book, chapter-1
  if (prevPage[1] < 0):
    prev_book_idx = current_book["idx"] - 1
    if (prev_book_idx < 0):
      prevPage = None, None
    else:
      prevBookInfos = ordered_books[prev_book_idx]
      prevPage = prevBookInfos, len(prevBookInfos) - 1

  nextPage = [current_book, chapter+1]
  if (nextPage[1] >= len(current_book["chapters"])):
    next_book_idx = current_book["idx"] + 1
    if next_book_idx >= len(ordered_books):
      nextPage = None, None
    else:
      nextBookInfos = ordered_books[next_book_idx]
      nextPage = nextBookInfos, 0

  return make_link(*prevPage), make_link(*nextPage)

def make_link(book_infos, chapter=None):
  if book_infos == None:
    return None
  
  if "url" in book_infos: return {
    "href": book_infos["url"],
    "label": book_infos["short"],
  }
  else: return {
    "label": f"{book_infos['short']} - {chapter+1}",
    "href": f"/chapter/{book_infos['id']}/{chapter+1}",
  }

def get_page_title(bookId:str, chapter:int, verseIdx:int=None):
  bookTitle = books[bookId]["short"]
  if chapter is not None and verseIdx is not None:
    return f"{bookTitle} {chapter+1}:{verseIdx}"
  if chapter is not None:
    return f"{bookTitle} {chapter+1}"
  else:
    return bookTitle

def get_verse_text(verse):
  return "".join([sentence["text"] for sentence in verse["sentences"]])

def get_verse_labels(verse):
  labels = set()
  for sentence in verse["sentences"]:
    labels.update(sentence["labels"])
  return labels

def get_chapter_labels(chapter):
  labels = set()
  for verse in chapter:    
    labels.update(get_verse_labels(verse))
  return labels

init()