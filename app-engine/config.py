labelMap = {
  "SPAM": { "color": '#228BEB', "name": 'spam', "detectedAs": "Spam-like" },
  "FLIRTATION": { "color": '#F66FD9', "name": 'flirtation', "detectedAs": "Flirtatious" },
  "PROFANITY": { "color": '#10803D', "name": 'profanity', "detectedAs": "Profane" },
  "IDENTITY_ATTACK": { "color": '#000000', "name": 'identity attack', "detectedAs": "Identity Attack" },
  "THREAT": { "color": '#EF2A2A', "name": 'threat', "detectedAs": "Threatening" },
  "INFLAMMATORY": { "color": '#EF2A2A', "name": 'provocation', "detectedAs": "Inflammatory" },  # Provocation is a (sort of) substantive for inflammatory
  "TOXICITY": { "color": '#6F32D3', "name": 'toxicity', "detectedAs": "Toxic" },
  "SEVERE_TOXICITY": { "color": '#6F32D3', "name": 'severe toxicity', "detectedAs": "Highly Toxic" },
  "SEXUALLY_EXPLICIT": { "color": '#F66FD9', "name": 'sexually explicit', "detectedAs": "Sexually Explicit" },
  "INSULT": { "color": '#F3890C', "name": 'insult', "detectedAs": "Insulting" },
  "OBSCENE": { "color": '#F66FD9', "name": 'obscenity', "detectedAs": "Obscene" },
}
for key in labelMap:
  labelMap[key]["id"] = key

baseUrl = "https://bible.artimproved.com"
baseUrl = "http://127.0.0.1:8080"
sharingDefaults = {
  "title": "The [safe] Holy Bible",
  "description": "Read the bible without the difficult parts, thanks to AI",
  "url": baseUrl,
  "image": f"{baseUrl}/assets/static_share/share_1.jpg",
}

# Any sentence with one of its scores >CENSOR_TRESHOLD will be censored
CENSOR_TRESHOLD = 0.7695