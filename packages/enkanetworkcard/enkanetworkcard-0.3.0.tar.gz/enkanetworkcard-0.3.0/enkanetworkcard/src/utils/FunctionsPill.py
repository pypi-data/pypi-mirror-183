# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image, ImageFont
from .openFile import *
from io import BytesIO
import requests
from cachetools import cached, TTLCache
        
@cached(cache=TTLCache(maxsize=1024, ttl=600))
def dowloadImg(link = "", image = None):
    if link != "":
        try:
            imgs = requests.get(link).content
        except:
            imgs = requests.get(link).content
    else:
        imgs = image
    return imgs

def imagSize(link = "", image = None, fixed_width = 0, size = None):
    if image:
        imgs = image
    else:
        imgs = Image.open(BytesIO(dowloadImg(link, image)))
    if size:
        new_image = imgs.resize(size)
    else:
        if imgs.size[0] != imgs.size[1]:
            ratio = (fixed_width / float(imgs.size[0]))
            height = int((float(imgs.size[1]) * float(ratio)))
            new_image = imgs.resize((fixed_width, height), Image.ANTIALIAS)
        else:
            new_image = imgs.resize((fixed_width,fixed_width))
    return new_image

@cached(cache=TTLCache(maxsize=1024, ttl=600))
def imgD(link = ""):
    imgs = Image.open(BytesIO(dowloadImg(link)))
    return imgs.convert("RGBA")

@cached(cache=TTLCache(maxsize=1024, ttl=600))
def centrText(text, witshRam = 100, razmer = 24, start = 0, Yram = 20, y = None, aling = "centry"):
    Text = ImageFont.truetype(font, razmer)
    maxDlina = witshRam
    while True:
        Text = ImageFont.truetype(font, razmer)
        withText = int(Text.getlength(str(text)))
        r = witshRam/2 
        t = withText/2 
        itog = r-t 
        if withText > maxDlina:
            razmer -= 1
            if razmer == 2:
                break
            continue
        break
    if y:
        while True:
            Text = ImageFont.truetype(font, razmer)
            HegText = Text.getbbox(str(text))[3]
            maxHeg = Yram
            r = Yram/2 
            t = HegText/2 
            itogs = r-t 
            if HegText > maxHeg:
                razmer -= 1
                if razmer == 2:
                    break
                continue
            break
        
        if aling == "centry":
            return (int(start + itog),int(y + itogs)),Text
        else:
            return (int(start),int(y)),Text

    if aling == "centry":
        return int(start + itog),Text
    else:
        return int(start),Text