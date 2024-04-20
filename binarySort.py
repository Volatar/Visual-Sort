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

#Testing: To be removed later
if __name__ == "__main__":
    # Create an Array object
    arr = Array(0)
    # Insert elements into the array
    arr.insert(0, 3)
    arr.insert(1, 1)
    arr.insert(2, 6)
    arr.insert(3, 2)
    arr.insert(4, 5)
    arr.insert(5, 4)
    arr.insert(6, 8)
    arr.insert(7, 7)
    # Output the unsorted array
    print("Unsorted Array:")
    print(arr)
    # Sort the array using binary sort
    sorted_arr = binarySort(arr.clone())
    # Output the sorted array
    print("Sorted Array:")
    print(sorted_arr)
