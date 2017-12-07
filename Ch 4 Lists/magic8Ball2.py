import random

messages = ['It is certain',
            'It is decidedly so',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My Reply is no',
            'Outlook not so good',
            'Very doubtful']

number = random.randint(0, len(messages) - 1)
print(f'Index: {number}')
print(messages[number])
