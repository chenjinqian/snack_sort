#-*- coding: utf-8 -*-
#!/usr/bin/python3
#Filename: buble_sort.py
#Author: JinQian Chen
#Email: 2012chenjinqian@gmail.com
#License: GPL

import randata
#get the random data.
imoport timeit
#count the time it use.

def buble_sort(a):
    """
    One of the simplest sort method.
    Arguments:
    - `a`:
    """
    length = len(a)-2
    i = 0
    cunt = 0
    while i < 1:
        j = 1
        while j>=i:
            if(a[j+1]<a[j]):
                a[j]
