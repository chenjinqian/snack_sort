#-*- coding: utf-8 -*-
#!/usr/bin/python2
print "This is the python2 expression"
#a = 0
#if 0 == a:
#    print("0 == a")
#else:
#    print("0 not equal to a")
#
#if a:
#    print("a")
#else:
#    print("a or 0 is NIL")
#
#if a-1 :
#    print("a - 1")
#else:
#    print("a or 0 is NIL")

#def test_while(size):
#    """
#
#    Arguments:
#    - `size`:
#    """
#    tmp = size
#    while size:
#        size -= 1
#        print("size", size)
#        print("tmp", tmp)

#sinal = [0]
#def sinal_plu(posi, num):
#    """
#
#    Arguments:
#    - `a`:
#    """
#    sinal[posi] += num

#def sinal_mes(posi, num):
#    """
#
#    Arguments:
#    - `a`:
#    """
#    sinal[posi] -= num

#the list can work as a global varient.
#import math
#math.exp(3)
#jump = 9
#if jump:
#    print("jump" , jump)

#pow(2, 10)  #1024
#import math
#help(math)
#import building
#print(dir(__builtins__))
#import randata
#import echo   #this is  a test new module.
#help(str)
#help(randata)
#help(0)
import media
#f = media.choose_file()
#import nose
#see test_quick_sort.

#tuple, once created, can not be changed.however, object inside it can still be changed.
#(5 + 3)
#(8,)
#life = (['canada', 75.5], ["US", 75], ['Mexico', 62])
#3 < 5 != True
#3 < 5 != False
#(3 < 5) != False
#for d in 'alpha':
#    print(d)
#
#import urllib
#help(urllib)
#dir(urllib)
import sys
def process_file(filenames):
    """open, read, and print a file.

    Arguments:
    - `filenames`:
    """
    input_file = open(filenames, "r")
    for line in input_file:
        line = line.strip()
        print(line)

    input_file.close()

print "This is the python2 expression"

if __name__ == "__main__":
    process_file(sys.argv[1])
