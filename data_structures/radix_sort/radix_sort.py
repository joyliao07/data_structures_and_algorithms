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
        """Tutorial: http://www.geekviewpoint.com/python/sorting/quicksort"""
        for i in self.lst:
            if isinstance(i, str):
                raise TypeError('Items must be integers.')
        self._quicksort(0, (len(self.lst)-1))

    def _quicksort(self, first, last):
        """Helper function for quickSort."""
        if first < last:
            # print('call partition: ', first, last)
            pivot = self.partition(first, last)
            # print('call _quick: ', first, pivot -1)
            self._quicksort(first, pivot - 1)
            # print('call _quick: ', pivot + 1, last)
            self._quicksort(pivot + 1, last)

    def partition(self, first, last):
        """Helper function for quickSort."""
        pivot = first + random.randrange(last - first + 1)
        # print('pivot is: ', pivot)
        # print('pivot - last: swap ', self.lst[pivot], ' with ', self.lst[last])
        self.swap(pivot, last)
        for i in range(first, last):
            # print('i is: ', i, ' first is: ', first)
            if self.lst[i] <= self.lst[last]:
                # print('i - first: swap ', self.lst[i], ' with ', self.lst[first])
                self.swap(i, first)
                first += 1

        # print('first - last: swap ', self.lst[first], ' with ', self.lst[last])
        self.swap(first, last)
        # print('return first: ', first)
        return first

    def swap(self, x, y):
        """Helper function for quickSort."""
        self.lst[x], self.lst[y] = self.lst[y], self.lst[x]

    def radixSort(self):
        for i in self.lst:
            if isinstance(i, str):
                raise TypeError('Items must be zero or positive integers.')
            if i < 0:
                raise KeyError('Items must be zero or positive integers.')

        # To find out how many times radix must be run:
        max_num = max(self.lst)
        exp = 1
        while max_num/exp > 1:
            self.radix_helper(exp)
            exp *= 10

    def radix_helper(self, exp):
        n = len(self.lst)

        # To create output list:
        output = [0] * (n)

        # To create 10 query buckets:
        count = [0] * (10)

        # Store count of occurrences in count[]

        # n = 5 the length of array:
        for i in range(0, n):
            index = (self.lst[i]/exp)
            count[int((index) % 10)] += 1

        # To reassign count[i] to help building the output:
        for i in range(1, 10):
            count[i] += count[i-1]

        # To build the output:
        i = n - 1
        while i >= 0:
            index = (self.lst[i]/exp)
            output[int(count[int((index) % 10)] - 1)] = self.lst[i]
            count[int((index) % 10)] -= 1
            i -= 1

        # To make the list copy the output list:
        i = 0
        for i in range(0, len(self.lst)):
            self.lst[i] = output[i]


# inpu = Sort([2, 41, -5, 9, 11, 5])

# inpu.radixSort()

# print(inpu.lst)
