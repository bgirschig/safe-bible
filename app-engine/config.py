# Sentence scores are stored in an array. This allows mapping values back to their label
SCORE_TYPES = ["SPAM","FLIRTATION","PROFANITY","IDENTITY_ATTACK","THREAT","INFLAMMATORY","TOXICITY","SEVERE_TOXICITY","SEXUALLY_EXPLICIT","INSULT","OBSCENE"]
score_labels = ['Spam-like', 'Flirtatious', 'Profane', 'Identity Attack', 'Threatening', 'Inflammatory', 'Toxic', 'Highly Toxic', 'Sexually Explicit', 'Insulting', 'Obscene']

color_map = [
  "#228BEB", # spam
  "#F66FD9", # flirt
  "#10803D", # profane
  "#000000", # Identity attack
  "#EF2A2A", # Threat
  "#EF2A2A", # inflammatory
  "#6F32D3", # Toxic
  "#6F32D3", # Higly Toxic
  "#F66FD9", # Sexually explicit
  "#F3890C", # Insult
  "#F66FD9", # Obscene
]

# Any sentence with one of its scores >CENSOR_TRESHOLD will be censored
CENSOR_TRESHOLD = 0.7695