import init_imgs
import sys

# test function.
# ideally this will move to parse.py, with init_imgs at the beginning and the lookup as a mapped command

d = init_imgs.get()
print('moving to slide number', d[sys.argv[1]], 'to find', sys.argv[1])