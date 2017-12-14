#! python3

"""
Regex Version of strip()
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
to the function will be removed from the string.
"""

import re


def regexstrip(stripstring, stripchars=None):   # assign default value of None in case only one arg gets passed, so it won't error
    if not stripchars:
        stripRegex = re.compile(r'^\s+|\s+$')
        stringstrip = stripRegex.sub('', stripstring)
    else:
        stripRegex = re.compile(r'[' + stripchars + ']')
        stringstrip = stripRegex.sub('', stripstring)
    return stringstrip

mystring = '          Ok this is a string test passing one argument to regexstrip'
mystring = regexstrip(mystring)
print(mystring)
print('Now passing two arguments, including chars to strip of sa:')
mystring = regexstrip(mystring, 'sa')
print(mystring)