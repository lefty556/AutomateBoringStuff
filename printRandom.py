import random

i = 0
print('Which # do you want to guess?')
guess = input()
while True:
    if i == 50:
        print('You exceeded 50 guesses and did not match the random number!')
        break;
    num = random.randint(1, 50)
    print(num)
    i += 1
    if num == int(guess):
        print('It took ' + str(i) + ' iterations to generate your matching number')
        break
