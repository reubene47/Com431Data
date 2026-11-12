import math

def BinarySearch(list, target):
    start = 0
    end = len(list) - 1
    midpoint = math.floor((start + end) / 2)

    while start <= end:
        if list[midpoint] == target:
            return f"{target} found at index {midpoint}"
        elif list[midpoint] > target:
            end = midpoint - 1
        else:
            start = midpoint + 1
        midpoint = math.floor((start + end) / 2)

    return f"Item {target} not in list"