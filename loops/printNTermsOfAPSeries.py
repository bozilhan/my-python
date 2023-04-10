# AP means arithmetic progression
# a is starting point 
# d is common difference
# n number of terms

a = int(input('starting point'))
d = int(input('common difference'))
n = int(input('number of terms'))

for term in range(a, n * d + a, d):
    print(term)