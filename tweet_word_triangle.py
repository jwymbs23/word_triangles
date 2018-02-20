import tweepy
from twitter_keys import *
import word_triangle as wt
import google_image_search as goog
import make_triangle as tri
import glob
import random
import time
import sys,os


if not os.path.exists('./downloads'):
    os.makedirs('./downloads')

if not os.path.exists('./triangles'):
    os.makedirs('./triangles')

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
#tweet = 'Hello, world!'

def post_saved():
    flist = glob.glob('./triangles/*.jpg')
    a = 1
    while a == 1:
        ind = random.randint(0,len(flist)-1)
        if flist[ind].find('_') != -1:
            a = 0
            imagename = flist[ind]
    print(imagename)
    words = imagename[12:-4].split('_')
    now = time.strftime("%c")
    api.update_with_media(imagename, status='It is ' + str(now) + ', and it is time for a word triangle. #' + words[0] + ' #' + words[1] + ' #' + words[2])


substrings, words = wt.pick_words()
search_fail = 0
for word in words:
    print(word)
    success = 0
    fail_count = 0
    while fail_count < 5:
        try:
            goog.search(word)
            fail_count = 6
            success = 1
            break
        except:
            fail_count  += 1
    if success != 1:
        if fail_count == 5:
            search_fail = 1
            break
if search_fail == 1:
    post_saved()
else:
    im_search_fail = 0
    im_fail_count = 0
    success = 0
    while im_fail_count < 5:
        try:
            imagename = tri.make_triangle(words[0], words[1], words[2], substrings[0], substrings[1], substrings[2], True)
            print(imagename)
            success = 1
            break
        except:
            im_fail_count += 1
        if success != 1:
            if im_fail_count == 5:
                im_search_fail = 1
                break
    print(imagename)
    if im_search_fail == 1:
        post_saved()
    else:
        now = time.strftime("%c")
        api.update_with_media(imagename, status='It is ' + str(now) + ', and it is time for a word triangle. #' + words[0] + ' #' + words[1] + ' #' + words[2])
