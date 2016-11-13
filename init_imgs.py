#!/usr/bin/env python
import os

def get():
	os.system('export GOOGLE_APPLICATION_CREDENTIALS=\'Presentalk-e0eb7b7c46fb.json\'')
	d = dict()
	os.system('ls parser | grep slide | wc -l > tmp.txt')
	with open('tmp.txt') as fh:
		length = int(fh.readlines()[0].rstrip().lstrip())
	for i in range(1, length+1):
		os.system('ls parser/slide'+str(i)+' > tmp.txt')
		with open('tmp.txt') as fh:
			for line in fh:
				filepath = 'parser/slide'+str(i)+'/'+line.rstrip()
				os.system('./label.py '+filepath+' > tmp2.txt')
				with open('tmp2.txt') as fh2:
					d[fh2.readlines()[0].split()[2]] = i
	os.system('rm tmp.txt')
	os.system('rm tmp2.txt')
	return d

	