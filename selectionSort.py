from dataStructures import Array


def selectionSort(array):
    # written by John Moukas
    # implement selection sort
    # output the contents of the array using the __str__ method each step of the way to show your work
    arrayLength = len(array)
    for i in range(arrayLength):
        min_idx = i
        for j in range(i+1, arrayLength):
            if array[j] < array[min_idx]:
                min_idx = j
        print(str(array))
        array[i], array[min_idx] = array[min_idx], array[i]
    
    return array
