#-*- coding: utf-8 -*-
#!/usr/bin/python3
#Filename: quick_sort_halfcopy.py
#Author: JinQian Chen
#Email: 2012chenjinqian@gmail.com
#License: GPL

#usage: copy and sort: quick_sort(list),
# destory original lists and sort: quick_sortN(list)

#copy number decrease from 4 times per fold to 3 times per fold, but the compare number increase 1 each fold. not sure how total  speed are.
#TODO, how to count the compare times, var global varient.

import randata
import copy

def mid (a, b , c):
    return max(min(a, b),min(max(a,b), c) )

def subsort(array, low, high):
    """
    Arguments:
    - `array`:
    - `low`:
    - `high`:
    """
    key = mid(array[low], array[high], array[int((low + high)/2)])
#    print("key is %d" % key)
#    key = array[low]
    for item in range(high - low + 1):  #this is because index is not fixed this time.
        if array[high] < key:
            tmp = array[low]
            array[low] = array[high]
            array[high] = tmp
            low += 1
#            print("low", low)
        else:
            high -= 1
    return low

def quick_sort(array_ori):
    array_cpy = copy.copy(array_ori)
#    array_cpy = copy.deepcopy(array_ori)
    return quick_sortNacc(array_cpy, 0, len(array_cpy) - 1)

def quick_sortN(array_ori):
    quick_sortNacc(array_ori, 0, len(array_ori) - 1)
    return array_ori


def quick_sortNacc(array, low, high):
    """
    quick_sortNacc fuction
    Arguments:
    - `array`:
    - `low`:
    - `high`:
    """
    if  low  >= high-1 :
        return subsort(array, low, high)
    else:
        index = subsort (array, low, high)
        quick_sortNacc(array, low, index - 1)
        quick_sortNacc(array, index , high)
    return array

if  __name__ == '__main__':
    print("quick sort half-copy example \n Usage: copy and sort: quick_sort(list) \n destory original lists and sort: quick_sortN(list)")
    array = randata.getran(20)
    print("Original array is" , array)
    print(quick_sort(array))

#ar = randata.getran(10)
#for test.
