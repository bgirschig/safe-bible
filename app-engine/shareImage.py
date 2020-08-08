from PIL import Image, ImageDraw, ImageFont
import os
from random import random, choice
from io import BytesIO
import math
import config

templatesDir = os.path.join("shareImage", "templates")
fontsDir = os.path.join("shareImage", "fonts")

backgrounds = []
for item in os.listdir(templatesDir):
  backgrounds.append(Image.open(os.path.join(templatesDir, item)))
font_address = ImageFont.truetype(os.path.join(fontsDir, "Roboto-Light.ttf"), size=50)
font_regular = ImageFont.truetype(os.path.join(fontsDir, "Roboto-Light.ttf"), size=35)
font_labels = ImageFont.truetype(os.path.join(fontsDir, "Roboto-Regular.ttf"), size=30)

def makeChapterImage(title, labels, chapter=1):
  img = choice(backgrounds).copy()
  draw = ImageDraw.Draw(img)
  width, height = img.size

  titleY = 130

  address = f"{title}\n\nChapter {chapter}"
  titleWidth = draw.multiline_textsize(address, font=font_address)[0]
  draw.multiline_text(((width-titleWidth)/2, titleY), address, fill="white", font=font_address, align="center")

  if labels:
    center_text(draw, width/2, 490, "Warning: This chapter contains verses detected as", font=font_regular)
    draw_labels(draw, img, labels, y=560)
  else:
    center_text(draw, width/2, 490, "This chapter was scanned by AI\nit is safe to read", font=font_regular)

  return to_jpeg(img)

def makeVerseImage(text, address, labels):
  img = choice(backgrounds).copy()
  draw = ImageDraw.Draw(img)
  width, height = img.size

  center_text(draw, width/2, 490, "This verse is hidden because it was detected as", font=font_regular)
  draw_labels(draw, img, labels, y=560)

  lineCount = min(math.floor(len(text)/50), 4)
  # lineCount = 1
  blockHeight = 40
  blocksY = 230 - ((lineCount+1)*blockHeight*1.5)/2
  # Draw text lines
  for idx in range(lineCount):
    y = blocksY + idx*blockHeight*1.5
    x = width/2
    lineWidth = 600+random()*200
    rectangle(draw, x+1, y+1, lineWidth, blockHeight, fill="#aaa")
    rectangle(draw, x, y, lineWidth, blockHeight, fill="black")
  # Draw address (eg. Genesis 3:14)
  center_text(draw, width/2, blocksY + lineCount*blockHeight*1.5+10, address, font_address)

  return to_jpeg(img)

def to_jpeg(img):
  img_io = BytesIO()
  img.convert("RGB").save(img_io, 'JPEG', quality=60)
  img_io.seek(0)

  return img_io

def draw_labels(draw, img, labels, y):
  # keep the top 5 labels
  labels = labels[:5]

  # First pass, to define the layout
  labelWidths = []
  textHeight = 0
  margin = 60
  for label in labels:
    size = draw.textsize(label["detectedAs"], font=font_labels)
    textHeight = size[1]
    labelWidths.append(size[0])
  # compute total width
  totalLabelWidth = sum(labelWidths) + margin*(len(labels)-1)
  labelsHeight = textHeight + 15

  # Second pass, for drawing
  currentX = (img.size[0] - totalLabelWidth) / 2
  for idx, label in enumerate(labels):
    # Draw "pill" background
    col = label["color"]
    draw.rectangle((currentX, y-labelsHeight/2, currentX + labelWidths[idx], y+labelsHeight/2), fill=col)
    circle(draw, currentX, y, r=labelsHeight/2, fill=col)
    circle(draw, currentX+labelWidths[idx], y, r=labelsHeight/2, fill=col)

    # Text
    draw.text((currentX, y-textHeight/2-3), label["detectedAs"], font=font_labels)

    # Update for next text
    currentX += labelWidths[idx] + margin

def center_text(draw, x, y, text, font):
  w, h = draw.multiline_textsize(text, font=font)
  draw.multiline_text((x-(w/2), y-(h/2)), text, font=font, align="center")

def rectangle(draw, x, y, width, height, **kwargs):
  draw.rectangle((x-width/2, y-height/2, x+width/2, y+height/2), **kwargs)

def circle(draw, x, y, r, **kwargs):
  draw.ellipse((x-r,y-r,x+r,y+r), **kwargs)

def drawPill(draw, x, y, width, height):
  pass
