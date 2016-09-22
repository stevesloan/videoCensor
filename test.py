#!/bin/python

import os
import subprocess

# answer = input("What would you like to do? ")

output = subprocess.check_output(['mkvinfo','/media/storage/Movies/the.lookout.2007.1080p.bluray.x264-hdmi.mkv'])
print ('Have %d bytes in output' % len(output))
output = output.decode("utf-8")

arList = output.split('\n| + A track')




def filterString(string, target):
    if string in target:
        return target
# arList = list(filter(filterString,arList))
arList = list(filter((lambda x: filterString('subtitles', x)),arList))


def splitStringColumns(listItem):
    out = listItem.split(':');
    if len(out) == 2:
        return {out[0]:out[1]}
    else:
        return False;



def splitString(listItem):
    out = listItem.split('\n|  + ');
    out = list(map(splitStringColumns,out));
    return out;

arList = list(map(splitString,arList));


# def arrayToObject(item):








def e(x):
    # out = list(filter())
    print(x)
list(map(e,arList))
