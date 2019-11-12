# GAME RULES
print('I AM A GUESSING GAME, I WILL ASK YOU TO ENTER A NUMBER')
print('IF YOUR GUESS IS GREATER THAN 100 OR LESS THAN ZERO IT WILL BE OUT OF BOUNDS')
print('on your first trial if your number is 10 closer or away from the number \ni will tell you warm or cold respectively')
print('if you guess the number i will congratulate you')
print('if you go further or closer from the number in your ubsequent guesses \ni will tell you colder or warmer respectively')


from random import randint

num = randint(1, 100)
print(num)

# save guesses in an empty list with zero as a placeholder
guesses = [0]


while True:
    guess = int(input('i have a secret number whats your guess?: '))

    if guess < 0 or guess > 100:
        print('OUT OF BOUNDS')
        continue

    if guess == num:
        print('CONGRATULATIONS YOU GUESSED THE NUMBER')
        break

    guesses.append(guess)


    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER')
        else:
            print('COLDER')
    
    else:
        if abs(num - guess) <= 10:
            print('WARM')
        else:
            print('COLD')
