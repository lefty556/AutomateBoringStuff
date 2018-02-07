#!/usr/bin/python3

# Write a program that finds all files with a given prefix, such as spam001.txt,
# spam002.txt, and so on, in a single folder and locates any gaps in the numbering
# (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
# Have the program rename all the later files to close this gap.

import os, pathlib, shutil


extensions = '.txt'

for filename in os.listdir('.'):
    if filename.endswith(extensions):
        name, ext = filename.split('.')
        if name[-3:].isdigit():
            print(filename)
#        if True:
#            print("File copied and overwritten.")
#            shutil.copy(filename, 'testdir')
