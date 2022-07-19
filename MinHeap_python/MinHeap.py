from heapq import heapify
import numpy as np
import math

HEAP_SIZE = 64

class MinHeap:
    def __init__(self):

        # Smallest empty index
        self.empty = 0

        # Size of the heap
        self.size = HEAP_SIZE

        # Backing array
        self.arr = np.zeros((HEAP_SIZE))

    def is_empty(self):
        return self.empty == 0

    def as_array(self):
        return self.arr

    def heapify_up (self, index):
        # The node at index i has children at indices 2i + 1 and 2i + 2; its parent is at floor ((i-1)/2)
        parent = math.floor((index - 1)/2)

        # If parent and child don't obey the min heap property, swap them
        if not (self.arr[parent] <= self.arr[index]):
            temp = self.arr[parent]
            self.arr[parent] = self.arr[index]
            self.arr[index] = temp
            
            # Recurse
            self.heapify_up(parent)

    def heapify_down (self, index):
        # The node at index i has children at indices 2i + 1 and 2i + 2; its parent is at floor ((i-1)/2)
        child_left = 2 * index + 1
        child_right = 2 * index + 2

        # Swap should be done with the smaller of the two children
        smallest = child_left if child_left <= child_right else child_right
        
        # If parent and child don't obey the min heap property, swap them
        if not (self.arr[index] <= self.arr[smallest]):
            temp = self.arr[index]
            self.arr[index] = self.arr[smallest]
            self.arr[smallest] = temp

            # Recurse
            self.heapify_down(smallest)

    def insert (self, element):
        if self.empty >= self.size:
            # If the array is too small, make a new array with double the size
            new_arr = np.zeros((self.size * 2))

            # Copy the old array to it
            new_arr[:len(self.arr)] = self.arr

            # Set the internal array to the new one, update size:
            self.arr = new_arr
            self.size = self.size * 2

        if self.empty == 0:
            self.arr[self.empty] = element
            self.empty = self.empty + 1
        else:
            self.arr[self.empty] = element
            self.heapify_up(self.empty)
            self.empty = self.empty + 1
