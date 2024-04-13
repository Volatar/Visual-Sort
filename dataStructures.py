class ArrayList(object):
    # written by Liwen Huang

    # for help making this work, see our lesson 4 lab

    # class variables
    # default variables should go here, such as a default size
    pass

    def __init__(self, sourceCollection = None):
        # creates object variables
        # you will need a list, logical size, and physical size
        pass

    def isEmpty(self):
        # checks if the array is currently empty
        pass

    def clear(self):
        # empties the array
        pass

    def append(self, item):
        # adds an item to the end of the array
        # make sure to check for array sizing and increase if needed
        pass

    def __str__(self):
        # returns a string representation of the array
        # do not include empty space in the array
        # this function is very important
        pass

    def __add__(self, other):
        # returns a new arrayList containing the contents of self and other combined
        # this is for when you do ArrayList + ArrayList
        pass

    def __eq__(self, other):
        # returns true if self and other contain the same information
        # false if they do not
        # iterate over the contents of both to do this
        pass

    def __contains__(self, item):
        # checks if the value of item is found in the array
        # return true if it is
        # return false if it is not
        # this is how we use the "in" operator
        pass

    def __getitem__(self, index):
        # access an item at the specified index
        pass

    def __setitem__(self, index, newItem):
        # replace the item at specified index
        pass

    def size(self):
        # return logical size
        pass

    def __grow(self):
        # increase the physical size of the array to double
        pass

    def __shrink(self):
        # decrease the physical size of the array by half
        pass

    def insert(self, index, newItem):
        # Inserts item at index in the array.
        pass

    def remove(self, index):
        # removes and returns item at index in the array
        pass

    def clone(self):
        # create a copy of this array and return it
        pass
