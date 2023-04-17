l1 = [3, 5, 7, 9, 3, 6, 5, 2, 3, 7, 10]
l2 = []

'''
TC: O(n)
SC: O(n)
'''
for l in l1:
    if l not in l2:
        l2.append(l)

'''
TC: O(nlogn + n)
SC: O(1)
'''
l1.sort();

'''
 reverse traversing
 [10:0:-1] -> [10:0) (negative step i.e. right to left <--- )
 '''
for i in range(len(l1) - 1, 0, -1):
    if l1[i - 1] == l1[i]:
        l1.pop(i)