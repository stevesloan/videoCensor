#!/bin/python
import subprocess
import sys

def parseMkvInfo(strInput):
    # split track info to array
    arList = strInput.split('\n| + A track')

    # remove non subtitle items
    def filterString(string, target):
        if string in target:
            return target
    arList = list(filter((lambda x: filterString('subtitles', x)),arList))

    # seperate line data by spliting ':'
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

    # rename this
    def splitString(listItem):
        out = listItem.split('\n|  + ');
        out = list(map(splitStringColumns,out));
        out = arrayToObject(out);
        return out;

    arList = list(map(splitString,arList));
    return arList

def help():
    print('Need file name')

def printPrompt(x):
    try:
        print(x['Language'] + " : " + x['Track_number'])
    except:
        print('');

def main():
    arg = sys.argv[1].pop(3)
    print(arg)
    if len(sys.argv) < 2:
        # help()
        # return False
        output = subprocess.check_output(['mkvinfo','/media/storage/Movies/the.lookout.2007.1080p.bluray.x264-hdmi.mkv']).decode("utf-8")
    else:
        # get data from mkvinfo
        output = subprocess.check_output(['mkvinfo',str(sys.argv[1])]).decode("utf-8")

    arList = parseMkvInfo(output)

    # print prompt
    list(map(printPrompt,arList))
    answer = input("Which track would you like to censor? ")





main()
