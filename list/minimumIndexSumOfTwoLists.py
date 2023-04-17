l1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
l2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

n = len(l1)
m = len(l2)
min = n + m

'''
TC: O(nm)
SC: O(1)
'''
for i in range(n):
    for j in range(m):
        if l1[i] == l2[j]:
            if i + j < min:
                min = i + j