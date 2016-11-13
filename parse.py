import voice
import re
import GoogleCSEGet
import os

# Command Functions
def next_slide(line):
	return -1

def back_slide(line):
	return -2

def go_to_slide(line):
  index = line.find('go to')
  words = line.split()
  if 'slide number' in line: # account for 'go to slide number x'
    try:
       num = int(words[words.index('number')+1])
    except:
      num = text2int(words[words.index('number')+1])
  else:
    try:
      num = int(words[words.index('slide')+1]) # 'go to slide x'
    except:
      num = 0
  # print(line)
  # print(num)
  return num

def go_to_image(line, d):
  index = line.find('go to')
  words = line.split()
  word = words[words.index('slide')+3]
  return d.get(word, 0)

def get_url(line):
  words = line.split()
  relevant_words = words[words.index('show')+2:]
  return GoogleCSEGet.get("%20".join(relevant_words))

def get_title(line, d): # return slide number with this title
  words = line.split()
  words = words[words.index('titled')+1:]
  for key in d.keys():
    if " ".join(words).lower().rstrip() in ' '.join(key.split()[0:10]).lower().rstrip(): # query only the first 10 words
      return d.get(key, 0)
  return 0

def search(line, d): # return first instance of slide with this text
  words = line.split()
  words = words[words.index('search')+2:]
  for key in d.keys():
    if " ".join(words).lower() in key.lower():
      return d.get(key,0)
  return 0

def zoom(line, d): # given any picture, find its filepath
  words = line.split()
  if 'picture' in words:
    word = words[words.index('picture')+3]
  else:
    word = words[words.index('zoom')+4]
  n = d.get(word,1)
  os.system('cp parser/slide'+str(n)+'/*.jpg viewer/assets/'+word+'.jpg')
  return '/assets/'+word+'.jpg'


# Returns an integer from a string
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current


trigger = 'slide'
trigger2 = 'show'
trigger3 = 'search'
trigger4 = 'zoom'
# regular expressions
keywords = {'next': next_slide,
            'forward': next_slide,
            'last': back_slide,
            'previous': back_slide,
            'back a slide': back_slide,
            'go.*to slide.*\d': go_to_slide,
            'go to.*slide with the \w': go_to_image,
            'show me \w+':get_url,
            'go to the slide titled \w+':get_title,
            'search for \w+':search,
            'zoom in.*the':zoom}

# Returns parsed voice command
def parse(d1, d2):
  line = voice.send_words()
  print(line)
  if line:
    for word in keywords.keys():
      if re.search(word, line) and (trigger in line or trigger2 in line or trigger3 in line or trigger4 in line):
        if word == 'go to.*slide with the \w' or word == 'zoom in.*the':
          return keywords[word](line,d1)
        elif word == 'go to the slide titled \w+' or word == 'search for \w+':
          return keywords[word](line,d2)
        else:
          return keywords[word](line)
  return 0