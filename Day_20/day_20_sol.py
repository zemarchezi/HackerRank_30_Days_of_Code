#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numberOfSwaps = 0
for i in range(0,len(a)):
    for j in range(0, (len(a)-1)):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]
            numberOfSwaps += 1

print ('Array is sorted in %d swaps.' % (numberOfSwaps))
print ('First Element: %d' % (a[0]))
print ('Last Element: %d' % (a[-1]))
            
