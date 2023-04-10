number = int(input('for me: enter number between 1 to 10'))

guess = 0;

while guess != number:
    guess = int(input('for your friend: enter your number'))

    if guess < number:
        print('smaller. enter greater than this')
    elif guess > number:
        print('greater. enter smaller than this')
    else:
        print('hit')