"""
This module implements of base sorting algorithms and allows simple time measurement for comparing them.
The accessible sorts may be found in function list.
"""
__author__ = 'Salmelu'

import random
import time
import heapq

def shell_sort(input_data, gap_sequence=None, verbose=False):
    """
    Sorts the given list data using shell sort and returns a new copy of sorted data.
    Allows to insert custom gap sequences, the default one is [701, 301, 132, 57, 23, 10, 4, 1],
    If verbose is set to true, prints how long the algorithm ran.
    """

    tstart = time.clock()
    if (not gap_sequence) or len(gap_sequence) < 1 or gap_sequence[-1] != 1:
        gap_sequence = [701, 301, 132, 57, 23, 10, 4, 1]
        n = 701
        while n < len(input_data):
            n = round(n*2.25)
            gap_sequence.insert(0, n)

    data = input_data.copy()
    t = 0

    for gap in gap_sequence:
        if gap >= len(data): continue
        for i in range(gap, len(data)):
            t = data[i]
            j = i
            while j >= gap and data[j-gap] >= t:
                data[j] = data[j-gap]
                j -= gap
            data[j] = t

    tend = time.clock()

    if verbose:
        print("Shell sort needed", (tend-tstart), "seconds to sort the data of size " + str(len(data)))
    return data


def heap_sort(input_data, verbose=False):
    """
    Sorts the given list data using heap sort and returns a new copy of sorted data.
    If verbose is set to true, prints how much time the algorithm needed.
    """
    tstart = time.clock()

    data = input_data.copy()

    length = len(input_data)
    heapq.heapify(data)
    datan = []

    for i in range(length):
        datan.append(heapq.heappop(data))

    tend = time.clock()
    if verbose:
        print("Heap sort needed", (tend-tstart), "seconds to sort the data of size " + str(len(datan)))
    return datan


def _quick_sort_in(input_data):
    """
    Intern method for quicksort
    """
    if input_data == []:
        return []
    else:
        pivot = input_data[0]
        first = _quick_sort_in([x for x in input_data[1:] if x < pivot])
        second = _quick_sort_in([x for x in input_data[1:] if x > pivot])
        return first + [pivot] + second


def quick_sort(input_data, verbose=False):
    """
    Sorts the given list data using quick sort and returns a new copy of sorted data.
     If verbose is set to true, prints how much time the algorithm needed.
    """

    tstart = time.clock()
    data = input_data.copy()

    _quick_sort_in(data)

    tend = time.clock()
    if verbose:
        print("Quick sort needed", (tend-tstart), "seconds to sort the data of size " + str(len(data)))
    return data


def merge_sort(input_data, verbose=False):
    """
    Sorts the given list data using merge sort and returns a new copy of sorted data.
     If verbose is set to true, prints how much time the algorithm needed.
    """

    tstart = time.clock()
    data = input_data.copy()
    data2 = data.copy()

    i = 0
    while 2**i < len(input_data):
        s1 = 0
        e1 = s1 + 2**i - 1
        s2 = e1 + 1
        e2 = s2 + 2**i - 1
        j = 0
        while s2 < len(input_data):
            if e2 >= len(input_data):
                e2 = len(input_data)-1
            while s1 <= e1 or s2 <= e2:
                if s2 > e2:
                    data2[j] = data[s1]
                    s1 += 1
                elif s1 <= e1 and data[s1] < data[s2]:
                    data2[j] = data[s1]
                    s1 += 1
                else:
                    data2[j] = data[s2]
                    s2 += 1
                j += 1
            s1 = e2 + 1
            e1 = s1 + 2**i - 1
            s2 = e1 + 1
            e2 = s2 + 2**i - 1
        data = data2
        data2 = data.copy()
        i += 1

    tend = time.clock()
    if verbose:
        print("Merge sort needed", (tend-tstart), "seconds to sort the data of size " + str(len(data)))
    return data


def select_sort(input_data, verbose=False):
    """
    Sorts the given list data using select sort and returns a new copy of sorted data.
     If verbose is set to true, prints how much time the algorithm needed.
    """

    tstart = time.clock()
    data = input_data.copy()

    q = 0
    min_index = 0

    for i in range(len(data)):
        min_index = i
        for j in range(i, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        q = data[i]
        data[i] = data[min_index]
        data[min_index] = q

    tend = time.clock()
    if verbose:
        print("Select sort needed", (tend-tstart), "seconds to sort the data of size " + str(len(data)))
    return data


def bubble_sort(input_data, verbose=False):
    """
    Sorts the given list data using bubble sort and returns a new copy of sorted data.
     If verbose is set to true, prints how much time the algorithm needed.
    """

    tstart = time.clock()
    data = input_data.copy()

    q = 0
    i = len(data)-1
    while i > 0:
        j = 0
        while j < i:
            if data[j] > data[j+1]:
                q = data[j]
                data[j] = data[j+1]
                data[j+1] = q
            j += 1
        i -= 1

    tend = time.clock()
    if verbose:
        print("Bubble sort needed", (tend-tstart), "seconds to sort the data of size " + str(len(data)))
    return data


def insert_sort(input_data, verbose=False):
    """
    Sorts the given list data using insert sort and returns a new copy of sorted data.
     If verbose is set to true, prints how much time the algorithm needed.
    """

    tstart = time.clock()
    data = input_data.copy()

    p = 0
    q = 0

    for i in range(1, len(data)):
        p = i-1
        q = data[i]
        while p >= 0:
            if data[p] > q:
                data[p+1] = data[p]
                p -= 1
            else:
                break
        data[p+1] = q

    tend = time.clock()
    if verbose:
        print("Insert sort needed", (tend-tstart), "seconds to sort the data of size " + str(len(data)))
    return data


def random_data(size):
    """
    Generates a list of integers from 0 to size-1, randomly shuffled.
    """
    data = list(range(size))
    random.shuffle(data)
    return data
