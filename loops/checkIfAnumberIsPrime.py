number = 7

for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0:
        print('not prime')
    else:
        print('prime')