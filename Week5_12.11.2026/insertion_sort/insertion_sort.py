def InsertionSort(list):
    for i in range(1, len(list)):
        current_value = list[i]
        position = i

        while position > 0 and list[position - 1] > current_value:
            list[position] = list[position - 1]
            position -= 1

        list[position] = current_value