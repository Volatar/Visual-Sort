class Array(object):
    # written by Liwen Huang
    # utilized the Array class from Lab 4
    

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        self.logicalSize = 0
        # Track the capacity and fill value for adjustments later
        self.capacity = capacity   # default capacity of the array
        self.fillValue = fillValue
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)
    
    def __add__(self, other):
        combined_list = Array()
        
        for anElement in self.items:
            combined_list.items.append(anElement)
            
        if isinstance(other, Array):
            for anElement in other.items:
                combined_list.items.append(anElement)
        else: 
            raise TypeError("Unsupported operand type for + 'ArrayList' and '{}'".format(type(other).__name__))
        
        return combined_list
    
    def __eq__(self , other):
        # returns true if self and other contain the same information
        # false if they do not
        if isinstance(other, Array):
            # Check if lengths are equal
            if len(self.items) != len(other.items):
                return False
            # Iterate over elements and compare
            for i in range(len(self.items)):
                if self.items[i]!= other.items[i]:
                    return False
            return True
        else: 
            return False
    
    def __contains__(self, item):
        # checks if the value of item is found in the array
        for anElement in self.items:
            if anElement == item:
                return True
        return False
    
    def __getitem__(self, index):
        """Subscript operator for access at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index.
        Precondition: 0 <= index < size()"""
        if index < 0 or index >= self.size():
            raise IndexError("Array index out of bounds")
        self.items[index] = newItem

    def size(self):
        """-> The number of items in the array."""
        return self.logicalSize

    def __grow(self):
        """Increases the physical size of the array if necessary."""
        # Double the physical size if no more room for items
        # and add the fillValue to the new cells in the underlying list
        for count in range(len(self)):
            self.items.append(self.fillValue)

    def __shrink(self):
        """Decreases the physical size of the array if necessary."""
        # Shrink the size by half but not below the default capacity
        # and remove those garbage cells from the underlying list
        newSize = max(self.capacity, len(self) // 2)
        for count in range(len(self) - newSize):   
            self.items.pop()

    def insert(self, index, newItem):
        """Inserts item at index in the array."""  
        if index < 0:
            index = 0
        elif index > self.logicalSize:
            index = self.logicalSize
        
        if len(self.items) == self.capacity:
            self.__grow()
        
        self.items.insert(index, newItem)
        self.logicalSize += 1    
        

    def remove(self, index):
        """Removes and returns item at index in the array."""
        try:
            if index < 0 or index >= self.logicalSize:
                raise IndexError("Array index out of bounds")
            
            remove_item = self.items.pop(index)
            self.logicalSize -= 1
            
            if (self.logicalSize <= self.capacity or self.logicalSize == 0.25 * self.capacity) and self.capacity >= 2 * self.capacity:
                self.__shrink()
        except IndexError as e:
            print(e)
        return remove_item

    def clear(self):
        """Removes all data items and resets the array to default."""
        self.items = [self.fillValue] * self.capacity
        self.logicalSize = 0

    def clone(self):
        """Creates and returns a clone of this Array object."""
        new_arr = Array(self.capacity, self.fillValue)
        new_arr.items = self.items.copy()
        new_arr.logicalSize = self.logicalSize
        return new_arr

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else: 
            return False
        
    