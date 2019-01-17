"""This module will contain class Hash and its related methods."""


class Hash(object):
    """
    """
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('Iterable is not a list.')

        self.len = 0
        self.lst = []

        for what in iterable:
            self.add_hash(what)

    def __repr__(self):
        output = f'<Hash table list: { self.lst }>'
        return output

    def __str__(self):
        output = f'Hash table length is { self.len }'
        return output

    def add_hash(self, val):
        """
        """
        if type(val) is not list:
            raise TypeError('Iterable is not a list with one key and one value.')

        if len(val) != 2:
            raise KeyError('Iterable is not a list with one key and one value.')

        # To obtain the index number:
        key = val[0]
        key_list = list(key)
        hash_num = 0
        for what in key_list:
            hash_num += ord(what)
        ind = hash_num // 10

        # If self.len is too short:
        if self.len <= ind:
            add = ind - self.len
            for what in range(add):
                self.lst.append([])
            self.len += add

        # To append the key-value pair:
        for what in self.lst[(ind-1)]:
            if what[0] == key:
                raise KeyError('Duplicated key.')

        self.lst[(ind-1)].append(val)

    def retrieve_val(self, key):
        """
        """
        # To obtain the index number:
        if key is None:
            raise TypeError('No key to look for.')

        key_list = list(key)
        hash_num = 0
        for what in key_list:
            hash_num += ord(what)
        ind = hash_num // 10

        if ind > self.len:
            print('No matching key is found.')
            return('No matching key is found.')

        for what in self.lst[(ind-1)]:
            if what[0] == key:
                print(what[1])
                return(what[1])

        print('No matching key is found')
        return('No matching key is found')

    def left_join(self, h2):
        print('left join here')
        shared = []
        for pair in self.lst:
            if len(pair) >= 1:
                for what in pair:
                    if pair[0] not in shared:
                        print('add: ', what)
                        # shared.add(pair)



h = Hash([['apple', 1], ['apple2', 2], ['banana', 3]])
h2 = Hash([['apple', 'apple in h2'], ['apple2', 'more apples in h2']])


# print(h.lst)
# print(str(h))
# print(repr(h))

h.left_join(h2)
