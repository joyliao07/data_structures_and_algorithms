"""This module contains the function multi_bracket_validation."""


def multi_bracket_validation(input):
    """To validate a string for multi-bracket."""
    temp = ''
    temp_str = input

    for what in temp_str:
        if what == '{' or what == '(' or what == '[':
            temp += what
            print('udpated temp is: ', temp)
        elif what == '}' or what == ')' or what == ']':
            # TO VALIDATE CLOSING BRACKET
            print('temp[-1] is: ', temp[-1])
            if what == '}':
                mirror = '{'
            elif what == ']':
                mirror = '['                
            elif what == ')':
                mirror = '('

            if mirror == temp[-1]:
                temp_str.replace(temp[-1], '', 1)
                temp_str.replace(what, '', 1)
                print('mirror is: ', mirror)
                temp = temp[:-1]
                print('updated temp is: ', temp)
            else:
                print(False)
                return False

    print(True)
    return True



str_ = '([]da[(]){()}s)'

multi_bracket_validation(str_)





