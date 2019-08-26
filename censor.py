#!/bin/python
import subprocess
import sys
import os


def parseMkvInfo(strInput):
    # split track info to array
    arList = strInput.split('\n| + Track')

    # remove non subtitle items
    def filterString(string, target):
        if string in target:
            return target

    arList = list(filter((lambda x: filterString('subtitles', x)), arList))

    # seperate line data by spliting ':'
    def splitStringColumns(listItem):
        out = listItem.split(':')
        if len(out) == 2:
            return [str.replace(out[0], ' ', '_'), out[1]]
        if len(out) == 3:
            return [str.replace(out[0], ' ', '_'), out[2]]
        else:
            return False

    def arrayToObject(list):
        obj = {}
        for item in list:
            if(item):
                obj.update({item[0]: item[1]})
        return obj

    # rename this
    def splitString(listItem):
        out = listItem.split('\n|  + ')
        # print(out)
        out = list(map(splitStringColumns, out))
        out = arrayToObject(out)
        return out

    arList = list(map(splitString, arList))
    return arList


def help():
    print('Need file name')


def printPrompt(x):
    prompt = ""
    try:
        prompt += x['Language']
    except:
        prompt += ""
    try:
        prompt += " - " + x['Name']
    except:
        prompt += ""
    try:
        prompt += " : " + x['Track_number']
    except:
        prompt += ""

    print(prompt)


def generateSrt():
    # validate that argument was given
    if len(sys.argv) < 2:
        help()
        return False
    else:
        # remove mkv file extension
        arg = sys.argv[1][:-4]

        # get data from mkvinfo
        output = subprocess.check_output(
            ['mkvinfo', arg+'.mkv']).decode("utf-8")
        output = subprocess.check_output(
            ['mkvinfo', arg+'.mkv']).decode("utf-8")
    # parse track listing
    arList = parseMkvInfo(output)

    # print prompt
    list(map(printPrompt, arList))
    answer = input("Which track would you like to censor? (x to use user supplied .srt file)")
    if answer == 'x':
        return
    command1 = arg + ".mkv"
    command2 = answer + ":" + arg + ".srt"
    subprocess.call(['mkvextract', 'tracks', command1, command2])
    # output = subprocess.check_output(['mkvextract', 'tracks '+ command1+ ' '+ command2])


def generateEdl():
    base_dir = os.path.dirname(os.path.realpath(__file__))
    arg = sys.argv[1][:-4]
    subprocess.call([base_dir + '/XBMC-Language-Filter/Linux/parse_srt.pl',
                     '--pad=0', "--offset=0", arg + ".srt"])


def main():
    generateSrt()
    generateEdl()


main()
