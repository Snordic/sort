#!/usr/bin/env python3.5
import random
import time


def create_array(length=100, maxint=100):
     new_arr=[random.randint(0, maxint) for _ in range(length)]
     return new_arr


def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i-1]>arr[i]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
                swapped=True
    return arr


def selection_sort(arr):
    sort_len=0
    while sort_len<len(arr):
        min_idx=None
        for i,elem in enumerate(arr[sort_len:]):
            if min_idx==None or elem<arr[min_idx]:
                min_idx=i+sort_len
        arr[sort_len], arr[min_idx]=arr[min_idx], arr[sort_len]
        sort_len+=1
    return arr


def insertion_sort(arr):
    for sort_len in range(1,len(arr)):
        cur_item = arr[sort_len]
        insert_idx = sort_len

        while insert_idx > 0 and cur_item < arr[insert_idx -1]:
            arr[insert_idx] = arr[insert_idx - 1]
            insert_idx += -1

        arr[insert_idx]=cur_item
    return arr


def merge(a,b):
    c = []
    a_idx, b_idx = 0, 0
    while a_idx<len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
        if a_idx == len(a): c.extend(b[b_idx:])
        else:               c.extend(a[a_idx:])
        return c


def merge_sort(arr):
    if len(arr)<=1: return arr
    left, right = merge_sort(arr[:int(len(arr)/2)]), merge_sort(arr[int(len(arr)/2):])
    return merge(left,right)


def quick_sort(arr):
    if len(arr) <= 1: return arr
    smaller ,equal, larger = [], [], []
    pivot = arr[random.randint(0, len(arr)-1)]

    for x in arr:
        if   x < pivot:    smaller.append(x)
        elif x == pivot:   equal.append(x)
        else:              larger.append(x)

    return quick_sort(smaller) + equal + quick_sort(larger)


def is_sorted(arr):
    for i in xrange(1, len(a)):
        if a[i]<a[i-1]: return False
    return True

def bogo_sort(arr):
    ct = 0
    while not is_sorted(arr):
        shuffle(arr)
        ct += 1
    return ct, arr

def binary_search(arr, val):
    if len(arr) == 0 or (len(arr) == 1 and arr[0] != val):
        return False
    mid = arr[len(arr)/2]
    if val == mid: return True
    if val < mid: return binary_search(arr[:int(len(arr)/2)], val)
    if val > mid: return binary_search(arr[int(len(arr)/2):], val)


def print_time(n=[10,100,1000,10000]):
    b0=[]
    b1=[]
    b2=[]
    b3=[]
    b4=[]
    b5=[]
    for length in n:
        arr=create_array(length, length)

        t0=time.time()
        s=sorted(arr)
        t1=time.time()
        b0.append(t1-t0)

        t0=time.time()
        s=bubble_sort(arr)
        t1=time.time()
        b1.append(t1-t0)

        t0=time.time()
        s=selection_sort(arr)
        t1=time.time()
        b2.append(t1-t0)

        t0=time.time()
        s=insertion_sort(arr)
        t1=time.time()
        b3.append(t1-t0)

        t0=time.time()
        s=merge_sort(arr)
        t1=time.time()
        b4.append(t1-t0)

        t0=time.time()
        s=quick_sort(arr)
        t1=time.time()
        b5.append(t1-t0)

    print("n\t Built-In \tBubble Sort \tSelection Sort \tInsertion Sort \tMerge Sort \tQuick Sort")
    print("________________________________"*3)
    for i, cur_n in enumerate(n):
        print("{0:}\t {1:.5f} \t{2:.5f} \t{3:.5f} \t{4:.5f} \t{5:.5f} \t{6:.5f}".format(cur_n, b0[i], b1[i], b2[i], b3[i], b4[i], b5[i]))


if __name__ == '__main__':
    print_time()
