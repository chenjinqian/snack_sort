#-*- coding: utf-8 -*-
#!/usr/bin/python3
#Filename: randata.py
#Author: JinQian Chen
#Email: 2012chenjinqian@gmail.com
#License: GPL

import random
def getran(num):
    a = []
    i = 0
    while i < num:
        a.append(random.randint(0, 1000000))
        i += 1
    return a

def getzero(num):
    a = []
    i = 0
    while i < num:
        a.append(0)
        i += 1
    return a
