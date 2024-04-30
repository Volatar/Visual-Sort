from dataStructures import Array


def insertionSort(array):
    # written by Morgan Roman Mach
    # implement insertion sort
    # output the contents of the array using the __str__ method each step of the way to show your work
    # Traverse through 1 to len(array)
    for i in range(1, array.size()):
        key = array[i]  # Select the current element to be compared

        # Move elements of array[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key  # Place the current element at its correct position

        # Output the contents of the array after each step
        print(array)
    return array
