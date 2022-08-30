# Stack Linked [Data Structure]
# Joshua Estrada

class Node:
    def __init__(self, data):
        self.data = data  # data stored by node
        self.next = None  # next reference


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  # set "capacity"
        self.top = None  # initialize top reference
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
        next_node = self.top
        self.top = Node(item)
        self.top.next = next_node
        self.num_items += 1
        # pushes item onto stack

    def pop(self):
        if self.is_empty():
            raise IndexError
        removed = self.top.data
        self.top = self.top.next
        self.num_items -= 1
        return removed
        # pops item from stack

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.top.data
        # returns item on top of stack

    def size(self):
        return self.num_items
        # return number of items in stack
