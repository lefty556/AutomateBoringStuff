#! python3
# selective copy - copy files with a given extention to a certain folder

import os


extensions = '.txt'

for filename in os.listdir(os.curdir):
    if filename.endswith(extensions):
        print(filename)