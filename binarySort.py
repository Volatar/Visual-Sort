from dataStructures import Array


def binarySort(array):
    # written by Morgan Roman Mach
    # Iterate over each element starting from the second one
    for i in range(1, array.size()):
        # Select the element to be inserted into the sorted portion
        current_element = array[i]
        # Perform binary search to find the correct position for insertion
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] < current_element:
                left = mid + 1
            else:
                right = mid - 1
        # Shift elements to make space for the current element
        for j in range(i, left, -1):
            array[j] = array[j - 1]
        # Insert the current element into its correct position
        array[left] = current_element
        # Output the contents of the array
        print(array)
    return array

