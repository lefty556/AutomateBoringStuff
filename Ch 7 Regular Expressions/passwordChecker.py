#! python3
import re
import sys

""" This checks the strength of a password.
Function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength

"""


"""
^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$

This regex will enforce these rules:
    At least one upper case English letter, (?=.*?[A-Z])
    At least one lower case English letter, (?=.*?[a-z])
    At least one digit, (?=.*?[0-9])
    Minimum eight in length .{8,} (with the anchors)
"""

def passwordCheck(password):
    passwordRegex = re.compile(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}')
    result = re.match(passwordRegex, password)

    if result:
        return True
    else:
        return False

numtries=0

while True:
    print('Please Enter a Password:')
    password = input()
    if passwordCheck(password):
        print('Password saved')
        print('Your password is {} characters long.'.format(len(password)))
        break
    else:
        if numtries == 3:
            print('Too many tries, exiting.')
            sys.exit(1)
        print('Password must contain uppercase, lowercase, and at least one digit.')
        numtries += 1
