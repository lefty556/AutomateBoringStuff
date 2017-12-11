#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text to the clipboard

import pyperclip

text = pyperclip.paste()

# seperate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]  # add start to each string in lines list

text = '\n'.join(lines)
pyperclip.copy(text)