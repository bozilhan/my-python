result = False

if x < 0 or (x > 0 and x % 10 == 0):
    result = False

number = 0
cloneX = x

while x > 0:
    number = number * 10 + x % 10
    x //= 10

result =  cloneX == number