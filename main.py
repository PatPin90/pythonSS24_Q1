import numpy as np
# importing the module to calculate execution time of functions

import timeit

# a list of numbers
numbers_list1 = [23, 104, 5, 190, 8, 7, -3]
numbers_list2 = []

# printing original lists
print("Input unsortierte Liste 1 : " + str(numbers_list1))
print("Input unsortierte Liste 2 : " + str(numbers_list2) + "\n")

# numbers_list3 =  random generate 1000000 integers
import random

numbers_list3 = []
n = 1000000
for i in range(n):
    numbers_list3.append(random.randint(0, 10000000))
# randint values are more than 1000000 on purpose to have a wider range than the final random numbers
#print("Input unsortierte random Liste 3 : " + str(numbers_list3))

# test case non-numeric list
numbers_list4 = ['a', 'b', 'c', 1, 2, 4]


# function to  get the indices of the sorted elements of given lists
def get_sorted_indices(numbers_list):
    sorted_indices = [i[0] for i in sorted(enumerate(numbers_list), key=lambda x: x[1])]
    return [(sorted_indices.index(i), numbers_list[i]) for i in range(len(numbers_list))]

# start timer to measure the processing time needed for executing the function on list 1
startL1 = timeit.default_timer()

if not numbers_list1:
    print("Error: The list 1 is empty.\n")
elif not all(isinstance(item, (int, float)) for item in numbers_list1):
    print("Error: The list 1 contains non-numeric values.\n")
else:
    res1 = get_sorted_indices(numbers_list1)
    print("Ergebnis: Sortierte Indexe aller Elemente der Liste 1 ohne NumPy: " + str(res1) + "\n")

#end timer
endL1 = timeit.default_timer()

# start timer to measure the processing time needed for executing the function on list 1
startL2 = timeit.default_timer()

if not numbers_list2:
    print("Error: The list 2 is empty.\n")
elif not all(isinstance(item, (int, float)) for item in numbers_list2):
    print("Error: The list 2 contains non-numeric values.\n")
else:
    res2 = get_sorted_indices(numbers_list2)
    print("Ergebnis: Sortierte Indexe aller Elemente der Liste 2 ohne NumPy: " + str(res2) + "\n")

#end timer
endL2 = timeit.default_timer()

# start timer to measure the processing time needed for executing the function on list 1
startL3 = timeit.default_timer()

if not numbers_list3:
    print("Error: The list 3 is empty.\n")
elif not all(isinstance(item, (int, float)) for item in numbers_list3):
    print("Error: The list 3 contains non-numeric values.\n")
else:
    res3 = get_sorted_indices(numbers_list3)
    print("Funktion zur Erstellung einer Liste der sortierten Indexe ohne NumPy für Liste 3 ist erfolgt.\n")
#    print("Ergebnis: Sortierte Indexe aller Elemente der Liste 3 ohne NumPy: " + str(res3))

#end timer
endL3 = timeit.default_timer()

# start timer to measure the processing time needed for executing the function on list 1
startL4 = timeit.default_timer()

# additional list to test case of error message if there are non-numeric values in the list
if not numbers_list4:
    print("Error: The list 4 is empty.\n")
elif not all(isinstance(item, (int, float)) for item in numbers_list4):
    print("Error: The list 4 contains non-numeric values.\n")
else:
    res4 = get_sorted_indices(numbers_list4)
    print("Ergebnis: Sortierte Indexe aller Elemente der Liste 4 ohne NumPy: " + str(res4) + "\n")

#end timer
endL4 = timeit.default_timer()

# get indices of all elements of the lists above with numpy
def get_sorted_indices_np(numbers_list):
    sorted_indices_np = np.argsort(numbers_list)
    return [(np.where(sorted_indices_np == i)[0][0], numbers_list[i]) for i in range(len(numbers_list))]

# result is shown in a tupel to also be able to directly see the corresponding element of the original, unsorted list

# start timer to measure the processing time needed for executing the function on list 1
startL1_np = timeit.default_timer()

if not numbers_list1:
   print("Error: The list 1 is empty.\n")
elif not all(isinstance(item, (int, float)) for item in numbers_list1):
   print("Error: The list 1 contains non-numeric values.\n")
else:
  res1_np = get_sorted_indices_np(numbers_list1)
  print("Ergebnis: Sortierte Indexe aller Elemente der Liste 1 MIT NumPy: " + str(res1_np) + "\n")

#end timer
endL1_np = timeit.default_timer()

# start timer to measure the processing time needed for executing the function on list 1
startL2_np = timeit.default_timer()

if not numbers_list2:
    print("Error: The list 2 is empty.\n")
elif not all(isinstance(item, (int, float)) for item in numbers_list2):
    print("Error: The list 2 contains non-numeric values.\n")
else:
    res2_np = get_sorted_indices_np(numbers_list2)
    print("Ergebnis: Sortierte Indexe aller Elemente der Liste 2 MIT NumPy: " + str(res2_np) + "\n")

#end timer
endL2_np = timeit.default_timer()

# start timer to measure the processing time needed for executing the function on list 1
startL3_np = timeit.default_timer()

if not numbers_list3:
    print("Error: The list 3 is empty.\n")
elif not all(isinstance(item, (int, float)) for item in numbers_list3):
    print("Error: The list 3 contains non-numeric values.\n")
else:
    res3_np = get_sorted_indices_np(numbers_list3)
    print("Funktion zur Erstellung einer Liste der sortierten Indexe MIT NumPy für Liste 3 ist erfolgt.\n")
#    print("Ergebnis: Sortierte Indexe aller Elemente der Liste 3 MIT NumPy: " + str(res3_np))

#end timer
endL3_np = timeit.default_timer()

# start timer to measure the processing time needed for executing the function on list 1
startL4_np = timeit.default_timer()

if not numbers_list4:
    print("Error: The list 4 is empty.\n")
elif not all(isinstance(item, (int, float)) for item in numbers_list4):
    print("Error: The list 4 contains non-numeric values.\n")
else:
    res4_np = get_sorted_indices_np(numbers_list4)
    print("Ergebnis: Sortierte Indexe aller Elemente der Liste 4 MIT NumPy: " + str(res4_np) + "\n")

#end timer
endL4_np = timeit.default_timer()

#compare execution times for functions above
# get execution time in milliseconds
resL1 = endL1 - startL1
final_resL1 = resL1 * 1000
final_resL1_rnd = round(final_resL1, 4)

resL2 = endL2 - startL2
final_resL2 = resL2 * 1000
final_resL2_rnd = round(final_resL2, 4)

resL3 = endL3 - startL3
final_resL3 = resL3 * 1000
final_resL3_rnd = round(final_resL3, 4)

resL4 = endL4 - startL4
final_resL4 = resL4 * 1000
final_resL4_rnd = round(final_resL4, 4)

resL1_np = endL1_np - startL1_np
final_resL1_np = resL1_np * 1000
final_resL1_np_rnd = round(final_resL1_np, 4)

resL2_np = endL2_np - startL2_np
final_resL2_np = resL2_np * 1000
final_resL2_np_rnd = round(final_resL2_np, 4)

resL3_np = endL3_np - startL3_np
final_resL3_np = resL3_np * 1000
final_resL3_np_rnd = round(final_resL3_np, 4)

resL4_np = endL4_np - startL4_np
final_resL4_np = resL4_np * 1000
final_resL4_np_rnd = round(final_resL4_np, 4)

print(f'CPU-gebundene Task-Zeit Liste 1, Funktion ohne NumPy: {final_resL1_rnd} Milisekunden')
print(f'CPU-gebundene Task-Zeit Liste 2, Funktion ohne NumPy: {final_resL2_rnd} Milisekunden')
print(f'CPU-gebundene Task-Zeit Liste 3, Funktion ohne NumPy: {final_resL3_rnd} Milisekunden')
print(f'CPU-gebundene Task-Zeit Liste 4, Funktion ohne NumPy: {final_resL4_rnd} Milisekunden' "\n")

print(f'CPU-gebundene Task-Zeit Liste 1, Funktion MIT NumPy: {final_resL1_np_rnd} Milisekunden')
print(f'CPU-gebundene Task-Zeit Liste 2, Funktion MIT NumPy: {final_resL2_np_rnd} Milisekunden')
print(f'CPU-gebundene Task-Zeit Liste 3, Funktion MIT NumPy: {final_resL3_np_rnd} Milisekunden')
print(f'CPU-gebundene Task-Zeit Liste 4, Funktion MIT NumPy: {final_resL4_np_rnd} Milisekunden' "\n")

print("Result comparision: using Python lists directly is more appropriate for small datasets, \nwhile NumPy is very fast in cases with big datasets, like list 3.")
