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
            # print('No matching key is found.')
            return('No matching key is found.')

        for what in self.lst[(ind-1)]:
            if what[0] == key:
                # print(what[1])
                return(what[1])

        # print('No matching key is found.')
        return('No matching key is found.')

    def left_join(self, h2):
        if self.lst == []:
            raise TypeError('No key to look for.')
        shared = []
        for place in self.lst:
            if len(place) >= 1:
                for what in place:
                    if what[0] not in shared:
                        shared.append(what)

        for pair in shared:
            retrieved_from_h2 = h2.retrieve_val(pair[0])
            print(retrieved_from_h2)
            if retrieved_from_h2 == 'No matching key is found.':
                pair.append('Null')
            else:
                # append value
                pair.append(retrieved_from_h2)
        # print(shared)
        return(shared)


# h1 = Hash([['apple', 1], ['apple2', 2], ['banana', 3]])
# h1 = Hash()
# h2 = Hash([['apple', 'apple in h2'], ['apple2', 'more apples in h2']])

# print(h.lst)
# print(str(h))
# print(repr(h))

# h1.left_join(h2)
