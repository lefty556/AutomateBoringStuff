def commacode(wordlist):
    newstring = ', '.join(wordlist).rsplit(',', 1)
    newstring = ' and'.join(newstring)
    return newstring

spam = ['apples', 'bananas', 'tofu', 'cats']
print(commacode(spam))