import voice

# Command Functions
def f1(line):
	return "*go to next slide*"

def f2(line):
	return "*go to previous slide*"

def f3(line):
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
      num = '?'
  return "moving to slide number " + str(num)

def f4(line, d):
  index = line.find('go to')
  words = line.split()
  word = words[words.index('slide')+3]
  return 'moving to slide number ' + str(d[word])


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
keywords = {'next': f1, 'forward': f1, 'last': f2, 'previous': f2,  'back': f2, 'go to slide': f3, 'go to the slide with the': f4}

# Returns parsed voice command
def parse(d):
  line = voice.send_words()
  if line:
    for word in keywords.keys():
      if word in line and trigger in line:
        if word == 'go to the slide with the':
          return keywords[word](line,d)
        else:
          return keywords[word](line)
  return ""