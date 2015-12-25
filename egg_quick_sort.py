#-*- coding: utf-8 -*-
#!/usr/bin/python3
#Filename: egg_quick_sort.py
#Author: JinQian Chen
#Email: 2012chenjinqian@gmail.com
#License: GPL

# I use to want reduce the copy time, by using group theory, interesting way, but not sure if it works. For simplity, here I directly move a string of elements,  hope there is a better way to do this.
#need N/2 space to speed up normal case, but make the worest situation worse.  Not neccery if use next method.
# I can update the ability of einpn funciton, if I can find the address directly, why do I mess up the ordered lists? In this way, I will not increase compare times, nore the data movement. So, this is at least as good as the previous one, not  mention this way can reduce funcal times.
# Another tips, If I have n/4 ordered serquence,  then it is effecient to use quick_sort and use bit-block-swap instead of move. The half of the fronter sorted is also likely to be the center of all unsorted elements.  break half.
import randata
import copy
# import quick_sort
#TODO, find that c function to fold a number by byte-moving.

def egg_sort (lst):
    lst_copy = copy.copy(lst)
    egg_sortNacc(lst_copy, 0, len(lst_copy) - 1, 0)
    return lst_copy

def egg_sortN(lst):
    """
    Arguments:
    - `lst`:     
    """
    egg_sortNacc(lst, 0, len(lst)-1, 0)
    return lst

# this double-N could  ref last version, but 
def egg_sortNacc(lst, start, end, N):
    """NOT YET.
    """

    egg_sortNacc(lst)
    print("function egg_sorNacc: lst, end, N, op, cl")

def ringBlockN(list, a, b, c, d):
    """This is like a ringN in block version, (a-b, c-d) --> (c-d, a-b). And, let d == c, this is the general version of ringN
    
    Arguments:
    - `list`:
    - `a`:
    - `b`:
    - `c`:
    - `d`:
    123456987
    987123456 (0, 5, 6, 8)
    987156234 (0, 3, 6, 8)  This is NOT  done yet.
    """
    lep = d - c + 1
    while c <= d :
        tmp = list[d]
        dfoot = d
        while dfoot > lep + a -1 :
            list[dfoot] = list[dfoot - lep]
            dfoot  -= lep
        list[dfoot]  = tmp
        d -= 1
    return lep


def bighalf(num):
    return twoexp(log2_int(num))  #get things more complicated,  there are quicker way to do this.

def egg_sortOneRun(lst, start, stop, N):
    steprint = twoexp(N) - 1 + start  #to be used as list index, so '-1'  here.
    center = start + twoexp(N -1)
    L = steprint + 1
    while stop > L :
        while lst[stop] > lst[center]:
            stop -= 1
#        while 

    swapnum = ringBlockN(lsa, center, steprint, steprint + 1, L)
    return swapnum
#        steprint += 1
#        jump = einpn(lst, steprint, N, steprint + 1)
#        print("steprint is" , steprint )
#        print("N is " , N)
#        print("jump is", jump)
#        if jump != twoexp(N):
#        sinal[steprint - twoexp(N) + 1] = 1

#    egg_sortOneRun(lst, )

def ringN(lst, ringend, jumpover):
    """
    Move the ring of (jumpover - 1) elements to right, and the most right element to the most left.
    No error check,  there should be check that (jumpover + 1) < len(lst), when call this function.
    Arguments:
    - `lst`: The list which all element are inside of it.
    - `ringend`: the right element of the ring.
    - `jumpover`: the jumpover of the ring.
    """

    tmp1 = lst[ringend]
    p = 0
    while jumpover - p :
        lst[ringend - p] = lst[ringend - p -1]
        p += 1
    lst[ringend - jumpover] = tmp1
#    print("ringinN: The end of ring is", tmp1)

def einpn(lst, eid, N, element):
    """
    Arguments:
    - `lst`:
    - `eid`:
    - `N`:
    - `element`:
    """
    if lst[element] < lst[eid - twoexp(N) + 1]:
#        print(lst[element], "einpn: Flyover" ,twoexp(N))
        return twoexp(N)
    else:
        if lst[element] >= lst[eid]:
#            print("einpn: 0 , element p[] " , element)
            return 0
    return e2pn(lst, eid, N, element)
#        print("trun to e2pn ")

def e2pn(lst, eid, N, element):
    """
    return relatively coordix after lg(N)+1 times compare.
    Arguments:
    - `lst`: the list.
    - `eid`: end of ordered number.
    - `N`: power of ordered number.
    - 'element': the element  to compare with and add in.
    """
    if  -1 ==N:
        return 0
    else:
        if lst[element] <= (lst[eid - twoexp(N - 1) + 1]):
            return twoexp(N - 1) + e2pn(lst, eid - twoexp(N - 1), N -1, element)
        else:
            return e2pn(lst, eid, N - 1, element)

def twoexp(N):
    """
    Arguments:
    - `N`:
    """
    if  -1 == N:
        return 0
    if 0 == N:
        return 1
    else:
        tmp = 2 * twoexp(N - 1)
    return tmp

def log2_int(N):
    """
    depend on math, there could be another way to do it. TODO.
    Arguments:
    - `N`:
    """
    from math import log2
    return int(log2(N))


lsa = [1,2,3,4,5,6,7,8,9,10,11,12, 13, 14, 15, 16, 24, 23, 22, 21, 20, 19, 18, 17, 32, 31, 30, 29, 28, 27, 26, 25]# for test.
#lsa = getran(32)
#lsa.reverse()
#return nonetype
