#-*- coding: utf-8 -*-
#!/usr/bin/python3
#Filename: quick_sort.py
#Author: JinQian Chen
#Email: 2012chenjinqian@gmail.com
#License: GPL

import randata
import copy

def subsort(array, low, high):
    """
    Arguments:
    - `array`:
    - `low`:
    - `high`:
    """
    key = array[low]
    for item in range(high - low):
        if array[high-item] < array[low]:
            array[low] = array[high-item]
            low += 1
            array[high-item] = array[low]
            array[low] = key
    return low

def quick_sort(array_ori):
    array_cpy = copy.copy(array_ori)
#    array_cpy = copy.deepcopy(array_ori)
    return quick_sortNacc(array_cpy, 0, len(array_cpy) - 1)

def quick_sortN(array_ori):
    return quick_sortNacc(array_ori, 0, len(array_ori) - 1)


def quick_sortNacc(array, low, high):
    """
    quick_sortNacc fuction
    Arguments:
    - `array`:
    - `low`:
    - `high`:
    """
    if  low >= high:
        return low
    else:
        index = subsort (array, low, high)
        quick_sortNacc(array, low, index - 1)
        quick_sortNacc(array, index + 1, high)
    return array

if  __name__ == '__main__':
    print("quick sort example")
    array = randata.getran(10)
    print(array)
    print(quick_sort(array))
    print(array)

#ar = randata.getran(10)
