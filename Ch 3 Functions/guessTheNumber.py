# This is a guess the number game.
import random


secretNumber = random.randint(1, 6)
print('I am thinking of a number between 1 and 6.')

# Ask the play to guess 6 times.
for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess == secretNumber:
        break
    elif guess < secretNumber:
        print('Your guess is too low')
    elif guess < secretNumber:
        print('Your guess is too high.')


if guess == secretNumber:
    print('Good job!  You guess my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
