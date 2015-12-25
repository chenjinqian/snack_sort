#-*- coding: utf-8 -*-
#!/usr/bin/python3
#Filename: quick_sort.py
#Author: JinQian Chen
#Email: 2012chenjinqian@gmail.com
#License: GPL

#usage: copy and sort: quick_sort(list),
# destory original lists and sort: quick_sortN(list)

import randata
import copy

#def mid (a, b , c):
#    return max(min(a, b),min(max(a,b), c) )

#def exg(a, b):
#    if a>b:
#        tmp = a
#        a =b
#        b = tmp
#    return (a,b)

def sort3N(lst,s,m,l):
    if lst[s] > lst[m]:
        tmp = lst[s]
        lst[s] = lst[m]
        lst[m] = tmp
    if lst[m] > lst[l]:
        tmp = lst[m]
        lst[m] = lst[l]
        lst[l] = tmp
    if lst[s] > lst[m]:
        tmp = lst[s]
        lst[s] = lst[m]
        lst[m] = tmp
    return lst

#not working
#another version.

def subsort(array, low, high):
    """
    Arguments:
    - `array`:
    - `low`:
    - `high`:
    """
#    key = mid(array[low], array[high], array[int((low + high)/2)])
#    print("key is %d" % key)
    sort3N(array, int((low + high)/2), low, high)
    key = array[low]
    for item in range(high - low):
        if array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
            array[low]= key
        else:
            high -= 1
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
    if  low  >= high -1:
        return subsort(array, low, high)
    else:
        index = subsort (array, low, high)
        quick_sortNacc(array, low, index - 1)
        quick_sortNacc(array, index + 1, high)
    return array


if  __name__ == '__main__':
    print("quick sort half-copy example \n Usage: copy and sort: quick_sort(list) \n destory original lists and sort: quick_sortN(list)")
    array = randata.getran(20)
    print("Original array is" , array)
    print(quick_sort(array))
#ar = randata.getran(10)
#for test
