arrays = []

while True:
    try:
        array = list(map(int, input().split()))
        arrays.append(array)
    except:
        break

def is_sorted_descending_safe(array):
    return all(array[i] > array[i + 1] and array[i] - array[i + 1] <= 3 for i in range(len(array) - 1))

def is_sorted_ascending_safe(array):
    return all(array[i] < array[i + 1] and array[i + 1] - array[i] <= 3 for i in range(len(array) - 1))

def is_sorted_descending_safe_v2(array):
    for i in range(len(array)):
        popped = array.pop(i)
        if is_sorted_descending_safe(array):
            return True
        array.insert(i, popped)
    return False

def is_sorted_ascending_safe_v2(array):
    for i in range(len(array)):
        popped = array.pop(i)
        if is_sorted_ascending_safe(array):
            return True
        array.insert(i, popped)
    return False

# Star 1
safe_arrays = 0
for array in arrays:
    if array[0] < array[1]:
        if is_sorted_ascending_safe(array):
            safe_arrays += 1
    else:
        if is_sorted_descending_safe(array):
            safe_arrays += 1

print(safe_arrays)
# Star 2
from copy import deepcopy
safe_arrays = 0
for array in arrays:
    result = is_sorted_ascending_safe_v2(deepcopy(array)) or is_sorted_descending_safe_v2(deepcopy(array))
    # if not result:
    #     print(array)
    safe_arrays += result

print(safe_arrays)