from pdfsplit import splitPages
import sys

def split(file_name, pg):
	splitPages(file_name, [slice(pg, pg+1, None)], "tmp/placeholder.pdf")

split(sys.argv[1], int(sys.argv[2]))