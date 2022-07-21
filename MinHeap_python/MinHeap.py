from heapq import heapify
import numpy as np
import math

MAX_HEAP_SIZE = 64

class MinHeap:
    def __init__(self):

        # Heap size
        self.heap_size = 0

        # Size of the heap
        self.max_size = MAX_HEAP_SIZE

        # Backing array
        self.arr = np.zeros((MAX_HEAP_SIZE))

    def is_empty(self):
        return self.heap_size == 0

    def as_array(self):
        return self.arr

    def get_heap_size(self):
        return self.heap_size

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
        # TODO Stop heapify_down if index's children are larger than heap_size/investigate further
        # The node at index i has children at indices 2i + 1 and 2i + 2; its parent is at floor ((i-1)/2)
        child_left = 2 * index + 1
        child_right = 2 * index + 2
        if child_left < self.heap_size and child_right < self.heap_size:

            # Swap should be done with the smaller of the two children
            smallest = child_left if self.arr[child_left] <= self.arr[child_right] else child_right
            
            # If parent and child don't obey the min heap property, swap them
            if not (self.arr[index] <= self.arr[smallest]):
                temp = self.arr[index]
                self.arr[index] = self.arr[smallest]
                self.arr[smallest] = temp

                # Recurse
                self.heapify_down(smallest)
        elif child_left < self.heap_size and not (child_right < self.heap_size):
            if not (self.arr[index] <= self.arr[child_left]):
                temp = self.arr[index]
                self.arr[index] = self.arr[child_left]
                self.arr[child_left] = temp

                # Recurse
                self.heapify_down(child_left)
        elif child_right < self.heap_size and not (child_left < self.heap_size):
            if not (self.arr[index] <= self.arr[child_right]):
                temp = self.arr[index]
                self.arr[index] = self.arr[child_right]
                self.arr[child_right] = temp

                # Recurse
                self.heapify_down(child_right)
        

    def insert (self, element):
        if self.heap_size >= self.max_size:
            # If the array is too small, make a new array with double the size
            new_arr = np.zeros((self.max_size * 2))

            # Copy the old array to it
            new_arr[:len(self.arr)] = self.arr

            # Set the internal array to the new one, update size:
            self.arr = new_arr
            self.max_size = self.max_size * 2

        if self.heap_size == 0:
            # Empty heap, just make it the root
            self.arr[self.heap_size] = element
            self.heap_size = self.heap_size + 1
        else:
            self.arr[self.heap_size] = element

            # Maintain the min heap property
            self.heapify_up(self.heap_size)
            self.heap_size = self.heap_size + 1

    def extract_min (self):
        # Swap the root with the last element (heap_size - 1)
        temp = self.arr[0]
        self.arr[0] = self.arr[self.heap_size - 1]
        self.arr[self.heap_size - 1] = temp

        # Decrease heap size
        self.heap_size = self.heap_size - 1

        # Maintain the heap property
        self.heapify_down(0)

        # Return extracted element
        return temp

