# Copyright 2022 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image, ImageChops
from .openFile import *
from .options import *
from .gradient import userAdaptGrandient
from cachetools import cached, TTLCache


def centryImage(userImages, teample = 1):
    if teample == 1:
        x,y = userImages.size
        baseheight = 1200

        if x > y or x == y:
            baseheight = 787
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.ANTIALIAS) 

        if x > y or x == y:
            return userImages, -int(userImages.size[0]/2-300)
        else:
            return userImages, -int(userImages.size[0]/2*0.2)
    elif teample == 2:
        x,y = userImages.size
        baseheight = 1500

        if x > y or x == y:
            baseheight = 1048
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.ANTIALIAS) 

        if x > y or x == y:
            return userImages, 0
        else:
            return userImages, 555
    else:
        x,y = userImages.size
        baseheight = 1337

        if x > y or x == y:
            baseheight = 802
        hpercent = (baseheight / float (y)) 
        wsize = int ((float (x) * float (hpercent)))
        userImages = userImages.resize ((wsize, baseheight), Image.ANTIALIAS) 

        if x > y or x == y:
            return userImages, 0
        else:
            return userImages, 0

def openImageElement(element,teample = 1):
    if teample == 1:
        if element == "Fire":
            bg = PyroBgTeampleOne.copy()
        elif element== "Grass":
            bg = DendroBgTeampleOne.copy()
        elif element == "Electric":
            bg = ElectroBgTeampleOne.copy()
        elif element == "Water":
            bg = GydroBgTeampleOne.copy()
        elif element == "Wind":
            bg = AnemoBgTeampleOne.copy()
        elif element== "Rock":
            bg = GeoBgTeampleOne.copy()
        elif element == "Ice":
            bg = CryoBgTeampleOne.copy()
        else:
            bg = ErrorBgTeampleOne.copy()
    elif teample == 2:
        if element == "Fire":
            bg = PyroBgTeampleTwo.copy()
        elif element== "Grass":
            bg = DendroBgTeampleTwo.copy()
        elif element == "Electric":
            bg = ElectroBgTeampleTwo.copy()
        elif element == "Water":
            bg = GydroBgTeampleTwo.copy()
        elif element == "Wind":
            bg = AnemoBgTeampleTwo.copy()
        elif element== "Rock":
            bg = GeoBgTeampleTwo.copy()
        elif element == "Ice":
            bg = CryoBgTeampleTwo.copy() 
        else:
            bg = ErrorBgTeampleTwo.copy()
    else:
        if element == "Fire":
            bg = PyroBgTeampleTree.copy()
        elif element== "Grass":
            bg = DendroBgTeampleTree.copy()
        elif element == "Electric":
            bg = ElectroBgTeampleTree.copy()
        elif element == "Water":
            bg = GydroBgTeampleTree.copy()
        elif element == "Wind":
            bg = AnemoBgTeampleTree.copy()
        elif element== "Rock":
            bg = GeoBgTeampleTree.copy()
        elif element == "Ice":
            bg = CryoBgTeampleTree.copy()
        else:
            bg = ErrorBgTeampleTree.copy()
    return bg
def openImageElementConstant(element, teampt = 1):
    if teampt in [1,2]:
        if element == "Fire":
            return PyroConstant.copy()
        elif element== "Grass":
            return DendroConstant.copy()
        elif element == "Electric":
            return ElectroConstant.copy()
        elif element == "Water":
            return GydroConstant.copy()
        elif element == "Wind":
            return AnemoConstant.copy()
        elif element== "Rock":
            return GeoConstant.copy()
        elif element == "Ice":
            return CryoConstant.copy()
        else:
            return ErrorConstant.copy()
    else:
        if element == "Fire":
            return PyroConstantOpen.copy(),PyroConstantClosed.copy()
        elif element== "Grass":
            return DendroConstantOpen.copy(),DendroConstantClosed.copy()
        elif element == "Electric":
            return ElectroConstantOpen.copy(), ElectroConstantClosed.copy()
        elif element == "Water":
            return GydroConstantOpen.copy(),GydroConstantClosed.copy()
        elif element == "Wind":
            return AnemoConstantOpen.copy(), AnemoConstantClosed.copy()
        elif element== "Rock":
            return GeoConstantOpen.copy(), GeoConstantClosed.copy()
        elif element == "Ice":
            return CryoConstantOpen.copy(), CryoConstantClosed.copy()
        else:
            return ErrorConstantOpen.copy(), ErrorConstantClosed.copy()
            
def maskaAdd(element,charter, teample = 1):
    if teample == 1:
        bg = openImageElement(element)
        bgUP = bg.copy()
        bg.paste(charter,(-734,-134),charter)
        im = Image.composite(bg, bgUP, MaskaBgTeampleOne.copy())
        bg.paste(im,(0,0))
    elif teample == 2:
        bg = openImageElement(element, teample = 2)
        bgUP = bg.copy()
        bg.paste(charter,(0,0),charter)
        im = Image.composite(bg, bgUP, MaskaSplas.copy())
        bg.paste(im,(0,0))
        bg.paste(MasskaEffectDown.copy(),(0,0),MasskaEffectDown.copy())
    else:
        bg = openImageElement(element, teample = 3)
        bgUP = bg.copy()
        bg.paste(charter,(-810,-115),charter)
        im = Image.composite(bg, bgUP, UserBgTeampleTree.copy())
        bg.paste(im,(0,0))
        bg.paste(EffectBgTeampleTree.copy(),(0,0),EffectBgTeampleTree.copy())
    return bg

def userImage(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img)
    if adaptation:
        grandient = userAdaptGrandient(userImagess.convert("RGB").copy())
        Effect = UserEffectTeampleOne.copy()
        grandient = ImageChops.screen(grandient,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(Effect, grandient, MaskaUserBg2TeampleOne.copy())
        return im
    else:
        try:
            bg = openImageElement(element)
            effect = bg.copy()
        except Exception as e:
            print(e)

        bg.paste(userImagess,(pozitionX,0))
        im = Image.composite(bg, effect, MaskaUserBg2TeampleOne.copy())
        bg.paste(im,(0,0))
        return bg


def userImageTree(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img, teample = 3)
    if adaptation:
        grandient = userAdaptGrandient(userImagess.convert("RGB").copy(), size =(1924,802))
        Effect = EffectBgTree.copy()
        grandient = ImageChops.screen(grandient,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(Effect, grandient, UserBgTeampleImgTree.copy())
        im.paste(EffectBgTeampleTree.copy(),(0,0),EffectBgTeampleTree.copy())
        return im
    else:
        bg = openImageElement(element, teample = 3)
        effect = bg.copy()
        bg.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(bg, effect, UserBgTeampleImgTree.copy())
        bg.paste(im,(0,0))
        bg.paste(EffectBgTeampleTree.copy(),(0,0),EffectBgTeampleTree.copy())
        return bg


def userImageTwo(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img, teample = 2)
    if adaptation:
        bg = openImageElement("error", teample = 2)
        grandientLeft = userAdaptGrandient(userImagess.convert("RGB").copy(), size = (1038, 1048),left = True)
        grandientRight = userAdaptGrandient(userImagess.convert("RGB").copy(), size = (937, 1048))
        bg.paste(grandientLeft,(0,0),grandientLeft)
        bg.paste(grandientRight,(grandientLeft.size[0],0),grandientRight)
        Effect = UserEffectTeampleTwo.copy()
        grandient = ImageChops.screen(bg,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(Effect, grandient, UserBgTeampleTwo.copy())
        return im
    else:
        bg = openImageElement(element, teample = 2)
        effect = bg.copy()
        bg.paste(userImagess,(pozitionX,0),userImagess)
        im = Image.composite(bg, effect, UserBgTeampleTwo.copy())
        bg.paste(im,(0,0))
        return bg


'''
def userImageBlur(img,element = None, adaptation = False):
    userImagess,pozitionX = centryImage(img)
    if adaptation:
        Effect = UserEffectTeampleOne.copy()
        bgBlur = userImagess.filter(ImageFilter.GaussianBlur(radius=80)).resize(Effect.size).convert("RGBA")
        bgBlur = ImageChops.screen(bgBlur,Effect)
        Effect.paste(userImagess,(pozitionX,0),userImagess)
        bg = Image.composite(Effect, bgBlur, MaskaUserBg2TeampleOne) 
        return bg
    else:
        img = openImageElement(element)
        effect = img.copy()
        img.paste(userImagess,(pozitionX,0))
        img.show()
        im = Image.composite(img, effect, MaskaUserBgTeampleOne)
        img.paste(im,(0,0))
        return img
'''
@cached(cache=TTLCache(maxsize=1024, ttl=600))
def star(x):
    if x == 1:
        imgs = Star1.copy()
    elif x == 2:
        imgs = Star2.copy()
    elif x == 3:
        imgs = Star3.copy()
    elif x == 4:
        imgs = Star4.copy()
    elif x == 5:
        imgs = Star5.copy()

    return imgs

@cached(cache=TTLCache(maxsize=1024, ttl=600))
def elementIconPanel(element):
    if element == "Fire":
        return PyroCharterElementTeampleTwo.copy()
    elif element== "Grass":
        return DendroCharterElementTeampleTwo.copy()
    elif element == "Electric":
        return ElectoCharterElementTeampleTwo.copy()
    elif element == "Water":
        return GydroCharterElementTeampleTwo.copy()
    elif element == "Wind":
        return AnemoCharterElementTeampleTwo.copy()
    elif element== "Rock":
        return GeoCharterElementTeampleTwo.copy()
    elif element == "Ice":
        return CryoCharterElementTeampleTwo.copy()
    else:
        return PyroCharterElementTeampleTwo.copy()

@cached(cache=TTLCache(maxsize=1024, ttl=600))
def getIconAdd(x, icon = False, size = None):
    if not icon:
        if not x in IconAddTrue:
            return False
    if x == "FIGHT_PROP_MAX_HP" or x == "FIGHT_PROP_HP":
        icons = FIGHT_PROP_MAX_HP.copy()
    elif x == "FIGHT_PROP_CUR_ATTACK" or x =="FIGHT_PROP_ATTACK":
        icons = FIGHT_PROP_CUR_ATTACK.copy()
    elif x == "FIGHT_PROP_CUR_DEFENSE" or x == "FIGHT_PROP_DEFENSE":
        icons = FIGHT_PROP_CUR_DEFENSE.copy()
    elif x == "FIGHT_PROP_ELEMENT_MASTERY":
        icons = FIGHT_PROP_ELEMENT_MASTERY.copy()
    elif x == "FIGHT_PROP_CRITICAL":
        icons = FIGHT_PROP_CRITICAL.copy()
    elif x == "FIGHT_PROP_CRITICAL_HURT":
        icons = FIGHT_PROP_CRITICAL_HURT.copy()
    elif x == "FIGHT_PROP_CHARGE_EFFICIENCY":
        icons = FIGHT_PROP_CHARGE_EFFICIENCY.copy()
    elif x == "FIGHT_PROP_ELEC_ADD_HURT":
        icons = FIGHT_PROP_ELEC_ADD_HURT.copy()
    elif x == "FIGHT_PROP_DEFENSE_PERCENT":
        icons = FIGHT_PROP_DEFENSE_PERCENT.copy()
    elif x == "FIGHT_PROP_ATTACK_PERCENT":
        icons = FIGHT_PROP_ATTACK_PERCENT.copy()
    elif x == "FIGHT_PROP_HP_PERCENT":
        icons = FIGHT_PROP_HP_PERCENT.copy()
    elif x == "FIGHT_PROP_WATER_ADD_HURT":
        icons = FIGHT_PROP_WATER_ADD_HURT.copy()
    elif x == "FIGHT_PROP_WIND_ADD_HURT":
        icons = FIGHT_PROP_WIND_ADD_HURT.copy()
    elif x == "FIGHT_PROP_ICE_ADD_HURT":
        icons = FIGHT_PROP_ICE_ADD_HURT.copy()
    elif x == "FIGHT_PROP_ROCK_ADD_HURT":
        icons = FIGHT_PROP_ROCK_ADD_HURT.copy()
    elif x == "FIGHT_PROP_FIRE_ADD_HURT":
        icons = FIGHT_PROP_FIRE_ADD_HURT.copy()
    elif x == "FIGHT_PROP_GRASS_ADD_HURT":
        icons = FIGHT_PROP_GRASS_ADD_HURT.copy()
    elif x == "FIGHT_PROP_HEAL_ADD":
        icons = FIGHT_PROP_HEAL_ADD.copy()
    elif x == "FIGHT_PROP_HEAL":
        icons = FIGHT_PROP_HEAL.copy()
    else:
        return False
    if size:
        icons.thumbnail(size)
        return icons.convert("RGBA")
    else:
        return icons.convert("RGBA")
