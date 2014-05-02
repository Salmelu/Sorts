__author__ = 'salmelu'

import sorts
import time
from functools import partial

# Helpful function definitions
output = open("testData", "w")
def generateData(power):
    return sorts.random_data(10**power)

gs1 = [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]
shell_sort_gap1 = partial(sorts.shell_sort, gap_sequence=gs1)
gs2 = [65921, 16577, 4193, 1073, 281, 77, 23, 8, 1]
shell_sort_gap2 = partial(sorts.shell_sort, gap_sequence=gs2)

# Variable definitions
constants1 = {2: 500,
              3: 100,
              4: 20}

sort_list1 = [sorts.insert_sort, sorts.bubble_sort, sorts.select_sort, sorts.merge_sort, sorts.quick_sort,
              sorts.heap_sort, sorts.shell_sort, shell_sort_gap1, shell_sort_gap2]
sort_name_list1 = ["Insert sort", "Bubble sort", "Select sort", "Merge sort", "Quick sort", "Heap sort",
                   "Shell sort with gaps [..., 701, 301, 132, 57, 23, 10, 4, 1]",
                   "Shell sort with gaps [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]",
                   "Shell sort with gaps [65921, 16577, 4193, 1073, 281, 77, 23, 8, 1]"]

constants2 = {2: 2000,
              3: 1000,
              4: 1000,
              5: 300,
              6: 5,
              7: 1}

sort_list2 = [sorts.merge_sort, sorts.quick_sort, sorts.heap_sort, sorts.shell_sort, shell_sort_gap1, shell_sort_gap2]
sort_name_list2 = ["Merge sort", "Quick sort", "Heap sort",
                   "Shell sort with gaps [..., 701, 301, 132, 57, 23, 10, 4, 1]",
                   "Shell sort with gaps [65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]",
                   "Shell sort with gaps [65921, 16577, 4193, 1073, 281, 77, 23, 8, 1]"]

# Starting tests

output.write("\n------------------------------------------------------------------------\n")
output.write("------------------------------ Tests 1 ---------------------------------\n")
output.write("------------------------------------------------------------------------\n\n")

for size in range(2, 5):
    test_result = {x: 0 for x in sort_list1}
    for n in range(constants1[size]):
        test_data = generateData(size)
        for func in sort_list1:
            start_time = time.clock()
            a = func(test_data)
            test_result[func] += time.clock() - start_time

    output.write("\n--------------------------- Data Size: " + str(10**size) + " -----------------------------\n")
    output.write("--------------------------- Test Count: " + str(constants1[size]) + " ----------------------------\n\n")
    for i in range(len(sort_list1)):
        output.write(sort_name_list1[i] + " took on average " + str(test_result[sort_list1[i]]/constants1[size])
                     + " seconds to sort data of size " + str(10**size) + ".\n")

output.write("\n------------------------------------------------------------------------\n")
output.write("----------------------------- Tests 1 end ------------------------------\n")
output.write("------------------------------------------------------------------------\n\n\n")

output.write("------------------------------------------------------------------------\n")
output.write("------------------------------ Tests 2 ---------------------------------\n")
output.write("------------------------------------------------------------------------\n")

for size in range(2, 8):
    test_result = {x: 0 for x in sort_list2}
    for n in range(constants2[size]):
        test_data = generateData(size)
        for func in sort_list2:
            start_time = time.clock()
            a = func(test_data)
            test_result[func] += time.clock() - start_time

    output.write("\n--------------------------- Data Size: " + str(10**size) + " -----------------------------\n")
    output.write("--------------------------- Test Count: " + str(constants2[size]) + " ----------------------------\n\n")
    for i in range(len(sort_list2)):
        output.write(sort_name_list2[i] + " took on average " + str(test_result[sort_list2[i]]/constants2[size])
                     + " seconds to sort data of size " + str(10**size) + ".\n")

output.write("\n------------------------------------------------------------------------\n")
output.write("----------------------------- Tests 2 end ------------------------------\n")
output.write("------------------------------------------------------------------------")
output.close()