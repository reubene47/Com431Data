import sys

def selection_sort(list):
    for i in range(len(list)-1):
        lowest_so_far = sys.maxsize
        for j in range(i, len(list)):