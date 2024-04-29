from random import randint
from dataStructures import Array

# Written by Taylor Sanderson


def randomArray():
    # create the array

    # get inputs on range of random numbers to use
    numberCount = int(input("How many numbers would you like in your array? (1-20): "))

    if numberCount < 1:
        numberCount = 1
    elif numberCount > 20:
        numberCount = 20

    maxNumber = int(input("How maximum would you like your random numbers to reach? (1-100): "))

    if maxNumber < 1:
        maxNumber = 1
    elif maxNumber > 100:
        maxNumber = 100

    numbers = Array(numberCount)

    # fill array with specified random values
    for i in range(numberCount):
        numbers.append(randint(1, maxNumber))

    return numbers
