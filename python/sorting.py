#! /usr/bin/python

'''
This code is to implement different sorting algorithm and compare the performance
'''
import random
import timeit
import copy
def swap(num, src, dest):
    tmp       = num[src]
    num[src]  = num[dest]
    num[dest] = tmp

def shuffle(num):
    size = len(num)
    for index in range(size):
        dest = index + random.randint(0, size-1-index)
        swap(num, index, dest)
    return num

def random_int(size):
    num = [0] * size
    for index in range(size):
        num[index] = random.randint(0, 1e7)
    return num

# O(N^2) time and O(1) space
def bubble_sorting(num):
    size = len(num)
    for i in range(0, size - 1):
        for j in range(size-2, i-1, -1):
            if num[j+1] < num[j]:
                swap(num, j, j+1)
            j -= 1
        i += 1

# O(N^2) time and O(1) space
def insert_sorting(num):
    size = len(num)
    for i in range(1, size):
        j = i
        while j > 0 and num[j-1] > num[i]:
            j -= 1
        num.insert(j, num[i])
        num.pop(i+1)

# O(NlogN) time and O(N) space
def heap_sorting(num):
    import heapq
    size = len(num)
    heap = list(num)
    heapq.heapify(heap)
    for index in range(size):
        num[index] = heapq.heappop(heap)

# Everything is here http://en.wikipedia.org/wiki/Shellsort
def shell_sorting(num):
    size = len(num)
    dist = size / 2
    while dist > 0:
        for i in range(dist, size):
            tmp = num[i]
            j = i
            while j >= dist and tmp < num[j - dist]:
                num[j] = num[j - dist]
                j -= dist
            num[j] = tmp
        dist /= 2

def merge_sorting(num):
    size = len(num)
    if size == 1:
        return num
    mid  = size / 2
    # splitting
    left_seq = merge_sorting(num[:mid])
    right_seq = merge_sorting(num[mid:])
    left_index, right_index, master_index = 0, 0, 0
    # merging
    while left_index < len(left_seq) and right_index < len(right_seq):
        if left_seq[left_index] < right_seq[right_index]:
            num[master_index] = left_seq[left_index]
            left_index += 1
        else:
            num[master_index] = right_seq[right_index]
            right_index += 1
        master_index += 1
    remain_num = left_seq if left_index < right_index else right_seq
    remain_index = left_index if left_index < right_index else right_index
    while remain_index <  len(remain_num):
        num[master_index] = remain_num[remain_index]
        remain_index += 1; master_index += 1
    return num

def partition(num, start, end):
    pivot_index = start
    pivot = num[start]
    for index in range(start, end + 1):
        item = num[index]
        if item < pivot:
            pivot_index += 1
            if pivot_index != index:
                swap(num, pivot_index, index)
    swap(num, pivot_index, start)
    return pivot_index

def quick_sorting_recursive(num, start, end):
    if start < end:
        split = partition(num, start, end)
        quick_sorting_recursive(num, start, split-1)
        quick_sorting_recursive(num, split+1, end)

def quick_sorting(num):
    quick_sorting_recursive(num, 0, len(num)-1)

def qsort(num):
    if len(num) == 0:
        return []
    pivot = num[0]
    left  = qsort([x for x in num[1:] if x < pivot])
    right = qsort([x for x in num[1:] if x >= pivot])
    return left + [pivot] + right

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def main():
    sample_size = [100,1000,10000]
    num_iteration = 10
    alg_dict = {'bubble': bubble_sorting, 'insert': insert_sorting, 'heap':   heap_sorting, 'quick':  qsort, 'shell':  shell_sorting}
    for size in sample_size:
        num = random_int(size)
        print "\nTesting sort algorithm with sample size: %d" % size
        for key in alg_dict.keys():
            copy_num = copy.copy(num)
            alg_wrapper = wrapper(alg_dict[key], copy_num)
            print '%s %s per iteration' % (key, timeit.timeit(alg_wrapper, number = num_iteration) / num_iteration)

if __name__ == '__main__':
    main()
