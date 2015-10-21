#-*- coding: utf-8 -*-
#!/usr/bin/python3
a = 0
if 0 == a:
    print("0 == a")
else:
    print("0 not equal to a")

if a:
    print("a")
else:
    print("a or 0 is NIL")

if a-1 :
    print("a - 1")
else:
    print("a or 0 is NIL")

def test_while(size):
    """

    Arguments:
    - `size`:
    """
    tmp = size
    while size:
        size -= 1
        print("size", size)
        print("tmp", tmp)

sinal = [0]
def sinal_plu(posi, num):
    """

    Arguments:
    - `a`:
    """
    sinal[posi] += num

def sinal_mes(posi, num):
    """

    Arguments:
    - `a`:
    """
    sinal[posi] -= num

#the list can work as a global varient.
import math
math.exp(3)
jump = 9
if jump:
    print("jump" , jump)
