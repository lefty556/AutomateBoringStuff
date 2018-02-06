#! python3
# listlargefiles.py - Lists files over 100 MB in a directory

import os


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


totalsize = 0;
maxsize = 1024 * 1024 * 500   # files over 500 MB

print('Printing files over {}:'.format(sizeof_fmt(maxsize)))
for folderName, subfolders, filenames in os.walk('C:\\Users\Diana\\Downloads'):
    for filename in filenames:
        totalsize = os.path.getsize(os.path.join(folderName, filename))
        if totalsize > maxsize:
            print(os.path.abspath(folderName) + '\\' + filename + ' : ' + str(sizeof_fmt(totalsize)))
