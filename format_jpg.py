#!/usr/bin/python2.7

import os, sys, re


def splitFile(file, names):
    if re.match('^\.', file) :
        return

    path = dir + file
    if os.path.isdir(path):
        return
    if file == 'Thumbs.db':
        return

    file = file.upper().strip()
    m = re.match('^([A-Z]+)-?(\d+).*(\.[a-zA-Z4]+)$', file)
    if not m :
        print 'jump:', file
        return
    name, code, t = m.groups()
    t = t.lower()
    if t != '.jpg':
        return
    if len(code) > 3:
        if code[:1] == '0':
            code = code[-3:]

    print 'new name:', name + '-' + code + t 

#    print 'new name:', new
    names[path] = name + '-' + code + t


def start(names):
    for key, value in names.items() :
        print 'move:', key, 'to', value
        os.system('mv "' + key + '" "' + value + '"')


for dir in sys.argv:
    if dir == sys.argv[0]:
        continue

    names = {}
    if os.path.split(dir)[1] != '':
        dir = dir + '/'

    list = os.listdir(dir)

    for file in list:
        #print 'start split:', file
        splitFile(file, names)

    start(names)
