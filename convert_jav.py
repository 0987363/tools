#!/usr/bin/python2.7

import os, sys, re

dir = sys.argv[1]
if os.path.split(dir)[1] != '':
    dir = dir + '/'

names = {}

def splitFile(file):
    if re.match('^\.', file) :
        return

    path = dir + file
    if os.path.isdir(path):
        return
    if file == 'Thumbs.db':
        return

    file = file.upper().strip()
    m = re.match('^([A-Z]+)-?(\d+).+$', file)
    if not m :
        return
    name, code = m.groups()
    if len(code) > 3:
        if code[:1] == '0':
            code = code[-3:]
    newName = dir + name + '-' + code

    if not names.get(newName) :
        names[newName] = []
    names[newName].append(path)

    print name + '-' + code, ":", file

def start():
    for key, value in names.items() :
        print 'mkdir:', key
        os.system('mkdir "' + key + '"')
        for item in value :
            print 'mv', item
            os.system('mv "' + item + '" "' + key + '"')

list = os.listdir(dir)
for file in list:
    print file
    splitFile(file)

start()
