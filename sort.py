
# 1. Bubble Sort

import mailcap
from operator import le


def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n):
        for j in range(0,n-i-1):
            if my_list[j]>my_list[j+1]:
                my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
    return my_list


# 2. Selection sort

def find_smallest_number(my_list):
    n=len(my_list)
    smallest_index=0
    for i in range(1,n):
        if my_list[smallest_index]>my_list[i]:
            smallest_index = i
    return smallest_index


def selection_sort(my_list):
    n= len(my_list)
    sorted_list=[]
    for i in range(n):
        temp_smallest = find_smallest_number(my_list)
        sorted_list.append(my_list.pop(temp_smallest))
    return sorted_list


# 3. merge sort

def merge_sort(my_list):
    n=len(my_list)
    if n > 1:
        mid = n // 2
        left = my_list[:mid]
        right = my_list[mid:]
        merge_sort(left)
        merge_sort(right)


        i = 0
        j = 0
        k = 0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                my_list[k]=left[i]
                i+=1
            else:
                my_list[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            my_list[k]=left[i]
            i+=1
            k+=1
        
        while j<len(right):
            my_list[k]=right[j]
            j+=1
            k+=1

    return my_list


# 4.Quick sort

def partition(my_list,left,right):
    i=left
    j=right-1
    pivot=my_list[right]

    while i < j:
        while i < right and my_list[i] < pivot:
            i+=1
        while j > left and my_list[j]>pivot:
            j-=1
        if i<j:
            my_list[i],my_list[j]=my_list[j],my_list[i]
    
    if my_list[i]>pivot:
        my_list[i],my_list[right]=my_list[right],my_list[i]
    return i


def quicksort(my_list,left, right):
    if left<right:
        index=partition(my_list,left,right)
        quicksort(my_list,left, index-1)
        quicksort(my_list,index+1,right)

the_list = [0,3,2,-4,10,12,-9,-4,1]

quicksort(the_list,0,len(the_list)-1)
print(the_list)