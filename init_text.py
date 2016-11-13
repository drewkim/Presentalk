import os

def get():
	d = dict()
	os.system('ls parser | grep slide | wc -l > tmp.txt')
	with open('tmp.txt') as fh:
		length = int(fh.readlines()[0].rstrip().lstrip())
	for i in range(1, length+1):
		try:
			with open('parser/slide'+str(i)+'/page'+str(i)+'.txt') as fh:
				d[fh.read()] = i
		except:
			pass
	os.system('rm tmp.txt')
	return d