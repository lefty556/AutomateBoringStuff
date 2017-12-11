def commacode(inputlist):
        if len(inputlist) == 1:
            return inputlist[0]
        return '{} and {}'.format(', '.join(inputlist[:-1]), inputlist[-1])


spam = ['apples', 'bananas', 'tofu', 'cats']
print(commacode(spam))
