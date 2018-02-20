import word_triangle as wt
import make_triangle as tri
import glob
import random
import time
import sys,os


if not os.path.exists('./downloads'):
    os.makedirs('./downloads')

if not os.path.exists('./triangles'):
    os.makedirs('./triangles')

substrings, words = wt.pick_words()
print(words, substrings)
imagename = tri.make_triangle(words[0], words[1], words[2], substrings[0], substrings[1], substrings[2], False)
print(imagename)

