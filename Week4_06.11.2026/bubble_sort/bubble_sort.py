# define bubble sort function with list parameter
def bubble_sort(list):
    # defined n to be the length of the list
    n = len(list)
    # loop through each iteration in length of list (n),
    # with -1 because if all the largest numbers are sorted then the smallest (first) number must also already be sorted
    for i in range(n-1):
        # loop through each iteration in length of list (n), minus the current iteration (i), minus 1
        for j in range(0, n-i-1):
            # check if the current number is greater than the next number
            if list[j] > list[j+1]:
                # if the current number is greater than the next number, swap the numbers
                list[j], list[j+1] = list[j+1], list[j]
    return list