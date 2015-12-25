#!/usr/bin/python3
#-*- coding: utf-8 -*-
#this should be the first line, to let it run properly.
#Filename: time-test.py
#Author: JinQian Chen
#Email: 2012chenjinqian@gmail.com
#License: GPL

#import time
import nose
#t1 = time.clock()
#a = 1+1
#t2 = time.clock()
#print(t2 - t1)
#print (time.timeit("a2 = 300 + 1000"))

import quick_sort
import egg_sneak_sort

def test_quick_sort ():
    """Test function for quick_sort
    """
    #pass
    assert quick_sort.quick_sort([9,8,5,7,6,4,2,3,1]) ==[1,2,3,4,5,6,7,8, 9]
    #assert quick_sort.quick_sort([9,8,5,7,6,4,2,3,1]) ==[1,2,3,4,5,6,7,9,8]

if __name__  == '__main__':
    nose.runmodule()

