# Written by Taylor Sanderson


def menu():

    # show the possible menu options
    print("\n\nSelect a menu option to try out")
    print("1: Try sorting my array with Bubble Sort")
    print("2: Try sorting my array with Binary Sort")
    print("3: Create new random numbers array")
    print("4: Exit program")

    # get user input
    choice = input("Choice: ")

    # check for bad inputs
    try:
        choice = int(choice)
    except:
        print("your choice must be a number from 1 to 4")
        return 0
    if choice < 0 or choice > 4:
        print("your choice must be a number from 1 to 4")
        return 0

    # return selected menu option index
    return choice
