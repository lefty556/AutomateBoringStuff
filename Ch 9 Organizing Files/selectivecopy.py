#! python3
# selective copy - copy files with a given extention to a certain folder

import os, pathlib, shutil


pathlib.Path('testdir').mkdir(parents=True, exist_ok=True)

extensions = '.txt'

for filename in os.listdir(os.curdir):
    if filename.endswith(extensions):
        print(filename)
        if os.path.isfile('testdir\\' + filename):
            print("This file exists already. Overwrite? (y/n)")
            overwrite = str(input().lower())
            if overwrite == 'y':
                print("File copied and overwritten.")
                shutil.copy(filename, 'testdir')

        else:
            print("File didn't exist.  Creating...")
            shutil.copy(filename, 'testdir')
