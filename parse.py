fh = open("speech.txt", "r")

def f1(line):
	print("*go to next slide*")

def f2(line):
	print("*go to previous slide*")

def f3(line):
	index = line.find('go to')
	num = int(line[index+12]) # account for 'go to slide x'
	print("moving to slide number", num)

keywords = {'next': f1, 'last': f2, 'go to': f3}

for line in fh:
	for word in keywords.keys():
		if word in line:
			keywords[word](line)

