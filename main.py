from bubbleSort import bubbleSort
from binarySort import binarySort
from selectionSort import selectionSort
from insertionSort import insertionSort
from dataStructures import Array
from menu import menu
from randomArray import randomArray


def main():
    # written by Taylor Sanderson
    skip = False

    numbers = randomArray()
    print("Your array is currently:")
    print(numbers)

    # present the menu with menu()
    choice = 0
    while True:
        choice = menu()

        # take menu return value and select operation
        if choice == 1:
            numbers = bubbleSort(numbers)
        if choice == 2:
            numbers = binarySort(numbers)
        if choice == 3:
            numbers = selectionSort(numbers)
        if choice == 4:
            numbers = insertionSort(numbers)
        if choice == 5:
            skip = True
        if choice == 6:
            break

        if not skip:
            print("Your array is now:")
            print(numbers)
            input("Press Enter to continue...")

        skip = False
        numbers = randomArray()
        print("Your new array of numbers is:")
        print(numbers)

main()
