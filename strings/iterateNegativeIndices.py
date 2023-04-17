s1 = 'Hello World'

'''
len: 11
range: [-11, 0)
step: -1
'''
for i in range(len(s1), 0, -1):
    print(s1[-i]) # -i !!!


'''
not hit the loop

len: 11
range: [-11, 0)
step: 1
'''
for i in range(len(s1), 0):
    print(s1[-i]) # -i !!!
else:
    print('not hit the loop')