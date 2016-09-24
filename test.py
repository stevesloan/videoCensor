#!/bin/python

import os
import subprocess

from functools import reduce



output = subprocess.check_output(['mkvinfo','/media/storage/Movies/the.lookout.2007.1080p.bluray.x264-hdmi.mkv'])
# print ('Have %d bytes in output' % len(output))
output = output.decode("utf-8")
# print (output)
arList = output.split('\n| + A track')


def test1():
    def test2(inp):
        return inp + 'test2'
    return 'test1'



def filterString(string, target):
    if string in target:
        return target

arList = list(filter((lambda x: filterString('subtitles', x)),arList))


def splitStringColumns(listItem):
    out = listItem.split(':');
    if len(out) == 2:
        return [str.replace(out[0], ' ', '_'),out[1]]
    if len(out) == 3:
        return [str.replace(out[0], ' ', '_'),out[2]]
    else:
        return False

def arrayToObject(list):
    obj = {};
    for item in list:
        if(item):
            obj.update({item[0]:item[1]})
    return obj;


def splitString(listItem):
    out = listItem.split('\n|  + ');
    out = list(map(splitStringColumns,out));
    out = arrayToObject(out);

    return out;



arList = list(map(splitString,arList));




# oList = reduce(lambda x,y: dict(x.items() + { y[0] : y[1]}), arList);
# oList = {x[0] : x[2] for x in arList}
# oList = dict(map(lambda x: [x[0], x[1]], arList))
# print(oList)
# obj.update(add_obj)





def printPrompt(x):
    try:
        print(x['Language'] + " : " + x['Track_number'])
    except:
        print('');
list(map(printPrompt,arList))

answer = input("What would you like to do? ")
