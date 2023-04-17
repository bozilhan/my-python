l1 = [10, 15, 6, 9, 12, 8, 4]
l2 = [14, 6, 19, 4, 7, 10, 11]
l3 = []

'''
TC: O(nm)
SC: O(n)
'''
for l in l1:
    if l  in l2:
        l3[len(l3):] = [l]
        # l3.append(l)

'''
TC: O(nlogn + mlogm + m + n)
SC: O(n)
'''
l4 = []

l1.sort()
l2.sort()

n = len(l1)
m = len(l2)

i = 0
j = 0

while i < n and j < m:
    if l1[i] == l2[j]:
        l4[len(l4):] = [l1[i]]
        i += 1
        j += 1
    elif l1[i] < l2[j]:
        i += 1
    else:
        j += 1

'''
TC: O(nlogn + nlogm)
SC: O(n)

Binary Search
'''
l1.sort()