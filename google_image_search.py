from apiclient.discovery import build
import urllib
from google_keys import *

def search(word):
    service = build("customsearch", "v1",developerKey=dev_key)
    #AIzaSyBHZcEBCvmq-MtQ0jA-tCxwbpbIv4LkL44")
    res = service.cse().list(
        q=word,
        cx=cse_id,
        searchType='image',
        num=2,
#        imgType='thumbnail',
        fileType='jpg',
        safe= 'high'
    ).execute()
    
    if not 'items' in res:
        print 'No result !!\nres is: {}'.format(res)
    else:
        for ci,item in enumerate(res['items']):
            print('\t{}'.format(item['link']))
            urllib.urlretrieve(item['link'], "./downloads/"+word+'_'+str(ci+1)+".jpg")
