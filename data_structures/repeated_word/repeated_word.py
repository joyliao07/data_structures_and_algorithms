"""This module will contain Hash class Hash and the method repeated_word that returns the first repeated word in a paragraph."""


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
        self.repeat = False

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

    def add_word(self, val):
        """
        """
        if val[0] is None:
            raise TypeError('No word in the string.')

        if self.repeat is True:
            return
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
                self.repeat = True
                print(what[0])
                return what[0]

        self.lst[(ind-1)].append(val)

    def repeated_word(self, string):
        """
        """
        if type(string) is not str:
            raise TypeError('Input is not a string.')
        
        if string is '':
            raise TypeError('No word in the string.')
        
        remove_punct = string.replace(',', '').replace('.', '').replace(';', '').replace('!', '').replace('+', '').lower()
        words_list = remove_punct.split(" ")
        for word in words_list:
            lst = [word, None]
            self.add_word(lst)
        if self.repeat is False:
            print('There is no repeated word in the paragraph.')
            return('There is no repeated word in the paragraph.')


# string = "apple"
# h = Hash()
# h.add_word(string)

# h = Hash([['apple', 1], ['apple2', 2], ['banana', 3]])

# print(h.lst)
# print(str(h))
# print(repr(h))

# h.retrieve_val('banana')












