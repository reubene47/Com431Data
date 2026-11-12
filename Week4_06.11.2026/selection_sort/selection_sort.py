import sys

def SelectionSort(list):
    for i in range(len(list)-1):
        lowest_so_far = list[i]
        lowest_index = i
        for j in range(i+1, len(list)):
            if list[j] < lowest_so_far:
                lowest_so_far = list[j]
                lowest_index = j
            elif list[j] > lowest_so_far:
                continue
            # swap lowest value with current value
        if lowest_index != i:
            list[i], list[lowest_index] = list[lowest_index], list[i]