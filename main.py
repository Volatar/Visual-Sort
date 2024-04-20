from bubbleSort import bubbleSort
from binarySort import binarySort
from dataStructures import Array
from menu import menu
from randomArray import randomArray


def main():
    # written by Taylor Sanderson

    numbers = randomArray()

    # present the menu with menu()
    choice = 0
    while True:
        print ("Your array is currently:")
        print(numbers)
        choice = menu()

        # take menu return value and select operation
        if choice == 1:
            numbers = bubbleSort(numbers)
        if choice == 2:
            numbers = binarySort(numbers)
        if choice == 3:
            numbers = randomArray()
        if choice == 4:
            break


main()
