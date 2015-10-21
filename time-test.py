#-*- coding: utf-8 -*-
#!/usr/bin/python3
#Filename: time-test.py
#Author: JinQian Chen
#Email: 2012chenjinqian@gmail.com
#License: GPL

import time
t1 = time.clock()
a = 1+1
t2 = time.clock()
print(t2 - t1)
print (time.timeit("a2 = 300 + 1000"))
