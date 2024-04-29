from dataStructures import Array


def bubbleSort(array):
    # written by John Moukas
    # implement bubble sort
    # output the contents of the array using the __str__ method each step of the way to show your work
    arrayLength = len(array)
    while arrayLength > 1:
        swapped = False
        i = 1
        while i < arrayLength:
            if array[i] < array[i - 1]:
                # Swap variables
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True
            i += 1
        print(str(array))
        if not swapped:
            break
        arrayLength -= 1
        
    return array


