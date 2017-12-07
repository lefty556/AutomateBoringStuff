def addcommas(input):
    message = ''
    i = 0
    j = len(input)
    for x in input:
        if i == j - 1:
            message = message + 'and ' + x
            break
        else:
            message = message + x + ', '
            i += 1
    return message


spam = ['apples', 'bananas', 'tofu', 'cats']

result = addcommas(spam)
print(result)
