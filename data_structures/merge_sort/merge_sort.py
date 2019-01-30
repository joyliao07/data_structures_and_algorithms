"""This module will contain class Sort and its related methods."""


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
        # output = f'Input list is { self.lst }'
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
        """Tutorial: https://www.geeksforgeeks.org/python-program-for-merge-sort/"""
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
            result = []
            while i < len(lefthalf.lst) and j < len(righthalf.lst):
                if lefthalf.lst[i] < righthalf.lst[j]:
                    self.lst[k] = lefthalf.lst[i]
                    result.append(lefthalf.lst[i])
                    i = i + 1
                else:
                    self.lst[k] = righthalf.lst[j]
                    result.append(righthalf.lst[j])
                    j = j + 1
                k = k + 1

            while i < len(lefthalf.lst):
                result.append(lefthalf.lst[i])
                self.lst[k] = lefthalf.lst[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf.lst):
                self.lst[k] = righthalf.lst[j]
                result.append(righthalf.lst[j])
                j = j + 1
                k = k + 1
            return result




# inpu = Sort([12, 11, 5, 7, 9])

# inpu.mergeSort()

# print(inpu)
# print(inpu.mergeSort())
