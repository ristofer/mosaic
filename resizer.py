#!/usr/bin/python
from PIL import Image
import os, sys

path = "/home/cristopher_gomez_ug_uchile_cl/artekis/artekis"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(path + "new/"+ item +' resized.jpg', 'JPEG', quality=100)

resize()