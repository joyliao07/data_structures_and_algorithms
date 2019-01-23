"""This module will contain class Sort and its related methods."""
import random


class Sort(object):
    """
    """
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('Input is not a list.')

        self.len = len(iterable)
        self.lst = iterable

    def __repr__(self):
        output = f'<Input list: { self.lst }>'
        return output

    def __str__(self):
        output = f'Input list length is { self.len }'
        return output

    def selection(self):
        """
        """
        for i in self.lst:
            if isinstance(i, str):
                raise TypeError('Items must be integers.') 

        for i in range(len(self.lst)):
            smallest_idx = i
            for a in range(i+1, len(self.lst)):
                if self.lst[smallest_idx] > self.lst[a]:
                    smallest_idx = a

            self.lst[i], self.lst[smallest_idx] = self.lst[smallest_idx], self.lst[i]
        return(self.lst)

    def mergeSort(self):
        print('argument is: ', self.lst)
        for i in self.lst:
            if isinstance(i, str):
                raise TypeError('Items must be integers.') 
        
        if len(self.lst) > 1:
            mid = len(self.lst)//2
            lefthalf = Sort(self.lst[:mid])
            righthalf = Sort(self.lst[mid:])

            lefthalf.mergeSort()
            righthalf.mergeSort()

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf.lst) and j < len(righthalf.lst):
                # print('in while loop, self.lst is: ', self.lst)
                # print('first loop position i is: ', i)
                if lefthalf.lst[i] < righthalf.lst[j]:
                    print('first loop position i is: ', i)
                    print('make self.lst[k] to be lefthalf.lst[i]: ', self.lst[k], lefthalf.lst[i])
                    self.lst[k] = lefthalf.lst[i]
                    i = i + 1
                else:
                    # print('first loop position j is: ', j)
                    # print('make self.lst[k] to be righthalf.lst[i]: ', self.lst[k], righthalf.lst[j])
                    self.lst[k] = righthalf.lst[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf.lst):
                # print('2nd loop position i is: ', i)
                # print('make self.lst[k] to be lefthalf.lst[i]: ', self.lst[k], lefthalf.lst[i])
                self.lst[k] = lefthalf.lst[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf.lst):
                # print('3rd loop position j is: ', j)
                # print('make self.lst[k] to be lefthalf.lst[i]: ', self.lst[k], righthalf.lst[j])
                self.lst[k] = righthalf.lst[j]
                j = j + 1
                k = k + 1

    def quickSort(self):
        print('quicksort')
        self._quicksort(0, (len(self.lst)-1))

    def _quicksort(self, first, last):
        """Helper function for quickSort."""
        if first < last:
            pivot = self.partition(first, last)
            self._quicksort(first, pivot - 1)
            self._quicksort(pivot + 1, last)

    def partition(self, first, last):
        """Helper function for quickSort."""
        pivot = first + random.randrange(last - first + 1)
        self.swap(pivot, last)
        for i in range(first, last):
            if self.lst[i] <= self.lst[last]:
                self.swap(i, first)
                first += 1

        self.swap(first, last)
        return first

    def swap(self, x, y):
        """Helper function for quickSort."""
        self.lst[x], self.lst[y] = self.lst[y], self.lst[x]


inpu = Sort([2, 1, 11, 4, 5, -11])

inpu.quickSort()
print(inpu.lst)
