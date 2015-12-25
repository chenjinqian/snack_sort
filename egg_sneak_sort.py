#-*- coding: utf-8 -*-
#!/usr/bin/python3
#Filename: egg-sneak-sort.py
#Author: JinQian Chen
#Email: 2012chenjinqian@gmail.com
#License: GPL

# I use to want reduce the copy time, by using group theory, interesting way, but not sure if it works. For simplity, here I directly move a string of elements,  hope there is a better way to do this.
#need N/2 space to speed up normal case, but make the worest situation worse.  Not neccery if use next method.
# I can update the ability of einpn funciton, if I can find the address directly, why do I mess up the ordered lists? In this way, I will not increase compare times, nore the data movement. So, this is at least as good as the previous one, not  mention this way can reduce funcal times.
# Another tips, If I have n/4 ordered serquence,  then it is effecient to use quick_sort and use bit-block-swap instead of move. The half of the fronter sorted is also likely to be the center of all unsorted elements.  break half
import randata
import copy
#import quick_sort
#TODO, find that c function to fold a number by byte-moving.


def egg_sort (lst):
    lst_copy = copy.copy(lst)
    egg_sortNacc(lst_copy, 0, len(lst_copy) - 1, 0)
    return lst_copy

def egg_sortN(lst, start, stop):
    """TODO: reload this funtion, make it work when called like this: egg_sortN(list) --> egg_sortN(list, 0, len(list)).
    Arguments:
    - `lst`:
    """
    if start > stop or stop > len(lst) - 1:
        print("egg_sortN: Parameter wrong.")
        return 0
    egg_sortNacc(lst, start, stop, 0)
    return lst

def egg_sortNacc(lst, lststart, lstend, N):
    """TODO: this job is done by subfuncall, but logically, this process can be in one line, and use some sinal to lineup
    """
    if lstend <= twoexp(N + 1) - 1:  #this place is weird,  with "=", the power can be 5 when there are only 32=2^5 elements. I have not notice that egg_sortOneRun can be called this way, which seems to be a coincident.
#        print("egg_sortOneRun(", lststart, lstend, N)
#  here I can use a if-expression to check lstend ?= twoexp(N),
        unfix = egg_sortOneRun(lst, lststart, lstend, N)
        print("unfix:" , unfix, "of power:", N)
        if 0 == unfix:
#            print("return: ", lstend)
            return lstend
    else:
#        print("double, N =", N)
#        print("egg_sortOneRun(", lststart, lststart + twoexp(N + 1) - 1, N)
        unfix = egg_sortOneRun(lst, lststart, lststart + twoexp(N + 1) - 1, N)

    if 0 != unfix:
        egg_sortNacc(lst, lststart, lststart + twoexp(N) - 1, log2_int(unfix))  #this place, a bug, I used to use beyhalf(unfix), this makes the property very veird.
#        print("double, N =", N + 1)
        egg_sortNacc(lst, lststart, lstend, N + 1)
    else:
#        print("double, N =" , N + 1)
        egg_sortNacc(lst, lststart, lstend, N + 1)
#    print("function egg_sorNacc: lst, end, N, op, cl")
#    sinal = [0 for i in range(beyhalf(N)) if 0]
# if I have run egg_onerun(lst, 31, 4), then the most repair work is egg_onerun(lst, 15, 3), no need to run egg_onerun(lst, 31, 4) again.


def beyhalf(num):
    """

    Arguments:
    - `num`:
    """
    return twoexp(log2_int(num))


def egg_sortOneRun(lst, start, stop, N):
    steprint = twoexp(N) - 1 + start  #to be used as list index, so '-1'  here.
    flyegg = 0
    while steprint < stop :
        jump = einpn(lst, steprint, N, steprint + 1)
        if jump == twoexp(N) and not flyegg:
            flyegg = steprint + 1 - twoexp(N)
        ringN(lst, steprint + 1, jump)
        steprint += 1
    return flyegg
#        print("steprint is" , steprint )
#        print("N is " , N)
#        print("jump is", jump)
#        if jump != twoexp(N):
#        sinal[steprint - twoexp(N) + 1] = 1
#   better use return value, instead of outside list.
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

#for test and debug during coding.
#lsa = [1,2,3,4,5,6,7,8,9,10,11,12,16,15,14,13]
#lsa = getran(32, 100)
#lsa.reverse()   #This will return nonetype.
