class Array(object):
    # written by Taylor Sanderson

    def __init__(self, capacity, sourceCollection = None):
        # creates object variables
        # you will need a list, logical size, and physical size
        if sourceCollection is None:
            self.items = []
        else:
            self.items = sourceCollection
        self.logicalSize = 0
        self.physicalSize = capacity

    def isEmpty(self):
        # checks if the array is currently empty
        if len(self.items) == 0:
            return True
        else:
            return False

    def clear(self):
        # empties the array
        self.items = []
        self.logicalSize = 0

    def append(self, item):
        # adds an item to the end of the array
        # make sure to check for array sizing and increase if needed
        if self.logicalSize == self.physicalSize:
            self.__grow()

        self.items.append(item)
        self.logicalSize += 1

    def __str__(self):
        # returns a string representation of the array
        # do not include empty space in the array
        # this function is very important
        return str(self.items)

    def __add__(self, other):
        # returns a new arrayList containing the contents of self and other combined
        # this is for when you do ArrayList + ArrayList
        while self.logicalSize + len(other) > self.physicalSize:
            self.__grow()

        combined = self.items
        count = self.logicalSize

        if isinstance(other, Array):
            for item in other:
                combined.append(item)
                count += 1
        else:
            raise TypeError("Unsupported operand type for + 'Array' and '{}'".format(type(other).__name__)) # this line written by Liwen

        combinedArray = Array(count, combined)
        return combinedArray

    def __eq__(self , other):  # written by Liwen
        # returns true if self and other contain the same information
        # false if they do not
        if isinstance(other, Array):
            # Check if lengths are equal
            if len(self.items) != len(other.items):
                return False
            # Iterate over elements and compare
            for i in range(len(self.items)):
                if self.items[i] != other.items[i]:
                    return False
            return True
        else:
            return False

    def __contains__(self, item):
        # checks if the value of item is found in the array
        # return true if it is
        # return false if it is not
        # this is how we use the "in" operator
        for items in self.items:
            if items == item:
                return True
        return False

    def __getitem__(self, index):
        # access an item at the specified index
        if index < 0 or index > self.logicalSize:
            raise IndexError("Index out of range: ", index)
        else:
            return self.items[index]

    def __setitem__(self, index, newItem):
        # replace the item at specified index
        if index < 0 or index > self.logicalSize:
            raise IndexError("Index out of range: ", index)
        else:
            self.items[index] = newItem

    def size(self):
        # return logical size
        return self.logicalSize

    def __grow(self):
        # increase the physical size of the array to double
        self.physicalSize = self.physicalSize * 2

    def __shrink(self):
        # decrease the physical size of the array by half
        self.physicalSize = self.physicalSize // 2

    def insert(self, index, newItem):
        # Inserts item at index in the array.
        self.items.insert(index, newItem)
        self.logicalSize += 1
        if self.logicalSize == self.physicalSize:
            self.__grow()

    def remove(self, index):
        # removes and returns item at index in the array
        returnValue = self.items.pop(index)
        self.logicalSize -= 1
        if self.logicalSize <= self.physicalSize // 2 and self.physicalSize > self.logicalSize:  # written by Liwen
            # Shrink the array
            self.__shrink()
        return returnValue

    def clone(self):
        # create a copy of this array and return it
        new = Array(self.physicalSize, self.items.copy())
        return new

    def __len__(self):
        return self.logicalSize
