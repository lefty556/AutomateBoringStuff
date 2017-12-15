#! python3

# Create a Mad Libs program that reads in text files and lets the user add
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
# appears in the text file.

# TODO:  Add ability to read file from command line arguments

import os, sys, re

if os.path.exists('madlibs.txt'):
    with open('madlibs.txt', 'r') as sourceFile:
        text = sourceFile.read()
else:
    sys.exit('Source File not found, please create')

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)|(ADVERB)')

for word in regex.findall(text):
    for match in word:
        if match != '':
            reg = re.compile(r'{}'.format(match))
            print('Please enter a {}:'.format(match))
            replace = str(input())
            text = reg.sub(replace, text, 1)

print(text)
with open('madlibs-outout.txt', 'w') as outFileObj:
    outFileObj.write(text)
