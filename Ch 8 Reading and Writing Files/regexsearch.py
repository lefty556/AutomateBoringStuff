#! python3
# regexsearch.py - a program that opens all .txt files in a folder and searches for any
# line that matches a user-supplied regular expression. The results should
# be printed to the screen.
# example:  regexsearch.py c:\users\diana

import sys, os


def usage():
    print('Usage: {} <directory>'.format(os.path.basename(__file__)))
    print('Example:  regexsearch.py c:\\users\\diana ')


def main(argv):
    # print command line arguments
    if len(argv) < 1:
        usage()
        sys.exit(1)
    folder = argv[0]
    if not os.path.exists(folder):
        sys.exit('Please enter a valid folder/directory')

    print('Enter a search string:')
    search = str(input())

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)   # get full path and filename joined up
        if os.path.isdir(path):
            continue
        if not filename.endswith('.txt'):   # only search for text files...
            continue
        print('Searching {} ...'.format(filename))
        with open(path, 'r') as searchfile:
            for num, line in enumerate(searchfile, 1):
                if search in line:
                    print('Line {}: {}'.format(num, line.rstrip()))  # print line num and strip \n from the line


if __name__ == '__main__':
    main(sys.argv[1:])
