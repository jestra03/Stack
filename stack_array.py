# Stack Array [Data Structure]
# Joshua Estrada

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  # set capacity [array size]
        self.items = [None] * capacity  # initialize array
        self.num_items = 0  # item counter

    def is_empty(self):
        return self.num_items == 0
        # checks if stack is empty

    def is_full(self):
        return self.num_items == self.capacity
        # checks if stack is full

    def push(self, item):
        if self.is_full():
            raise IndexError
        self.items[self.num_items] = item
        self.num_items += 1
        # pushes item onto stack

    def pop(self):
        if self.is_empty():
            raise IndexError
        self.num_items -= 1
        return self.items[self.num_items]  # returns "popped" item
        # pops item from stack

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.items[self.num_items - 1]
        # returns item on top of stack

    def size(self):
        return self.num_items
        # returns number of items in stack
