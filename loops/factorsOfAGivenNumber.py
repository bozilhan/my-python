import math

number = 36

for i in range(1, int(math.sqrt(number)) + 1):
    if number % i == 0:
        # if divisors are equal, print only one
        if number // i == i:
            print(i)
        else:
            print(i, number // i)