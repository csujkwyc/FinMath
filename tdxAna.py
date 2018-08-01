# -*- coding: utf-8 -*-

from struct import *
from math import *
import csv
import os

dic_day = {}
dic_5min = {}
dic_1min = {}



def deal_with_day(ifile):
    if ifile == None:
        return

    result = []
    fmt = '<IIIIIfII'
    segment = calcsize(fmt)

    with open(ifile, "rb") as fp:
        daybuf = fp.read()
        begin = 0
        for i in range(int(len(daybuf)/segment)):
            result.append( unpack(fmt, daybuf[begin:begin+segment]))
            begin += segment             
    return (result)


def deal_with_5min(ifile):
    if ifile == None:
        return 
    result = []
    fmt = '<hhfffffIi'
    segment = calcsize(fmt)

    with open(ifile, "rb") as fp:
        fiveminbuf = fp.read()
        begin = 0
        for i in range(int(len(fiveminbuf)/segment)):
            t = unpack(fmt, fiveminbuf[begin:begin+segment])
            tmpdate = str(floor(t[0]/2048)+2004) + str(floor((t[0]%2048)/100)).zfill(2) + str((t[0]%2048)%100).zfill(2)
            result.append([tmpdate, t[1], t[2], t[3], t[4], t[5], t[6], t[7]])
            begin += segment
    
    return result

def deal_with_1min(ifile):
    if ifile == None:
        return 

    result = []
    fmt = '<hhfffffIi'
    segment = calcsize(fmt)

    with open(ifile, "rb") as fp:
        oneminbuf = fp.read()
        begin = 0
        for i in range(int(len(oneminbuf)/segment)):
            t = unpack(fmt, oneminbuf[begin: begin+segment])
            tmpdate = str(floor(t[0]/2048)+2004) + str(floor((t[0]%2048)/100)).zfill(2) + str((t[0]%2048)%100).zfill(2)
            result.append([tmpdate, t[1], t[2], t[3], t[4], t[5], t[6], t[7]])
            begin += segment
    
    return result


def filenames_from_folder(folder, postfix):
    L = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if os.path.splitext(file)[1] == postfix:
                L.append(os.path.join(root, file))
    return L


def main():


    print ("Deal with day line.")
    L = filenames_from_folder("C:\\zd_pazq\\vipdoc\\sz\lday\\", ".day")
    for filename in L:
        res = deal_with_day(filename)
        dic_day[os.path.basename(filename)] =res
        #with open("d:\\temp\\20180731\\day\\"+os.path.basename(filename)+".csv", "w+", newline='') as f:
        #    writer = csv.writer(f)
        #    writer.writerows(res)
    
    print ("\nDeal with 5min line.")
    L = filenames_from_folder("C:\\zd_pazq\\vipdoc\\sz\\fzline\\", ".lc5")
    for filename in L:
        res = deal_with_5min(filename)
        dic_5min[os.path.basename(filename)] = res
        #with open("d:\\temp\\20180731\\fzline\\"+os.path.basename(filename)+".csv", "w+", newline='') as f:
        #    writer = csv.writer(f)
        #    writer.writerows(res)

    print ("\nDeal with 1min line.")
    L = filenames_from_folder("C:\\zd_pazq\\vipdoc\\sz\\minline\\", ".lc1")
    for filename in L:
        res = deal_with_1min(filename)
        dic_1min[os.path.basename(filename)] = res
        #with open("d:\\temp\\20180731\\minline\\"+os.path.basename(filename)+".csv", "w+", newline='') as f:
        #    writer = csv.writer(f)
        #    writer.writerows(res)
    pass


if __name__ == "__main__":
    main()
    input("Press Enter to continue...")

