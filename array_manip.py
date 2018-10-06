# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 10:53:47 2018

@author: sdh
"""

#exploring 2D arrays

import numpy as np
from scipy import stats

r0 = []
r1 = [1,2,3,4]
r2 = [2,4,6,8]
r3 = [3,6,9,12]

array_a = ([r1])  #r1 is alread and array, so [r1] is a 2D array. 
print(array_a)

array_a.append(r3)
print(array_a)

array_a = [r1, r2]
array_b = [r1,r2,r3]
print(array_a)

array_a.append(r3)
print(array_a)

array_c = []
array_c.append(r1)
print (array_c)

print(np.mean(array_a), np.mean(array_a, axis=0), np.mean(array_a, axis=1))
x = range(3)

c1 = [1,2,3]
c2 = [2,4,6]
c3 = [3,6,9]
c4 = [4,8,12]
array_d = []
for i in range(len(c1)):
    row = [c1[i],c2[i],c3[i],c4[i]]
    array_d.append(row)
print(array_d)
#print(stats.linregress(x,array_a[0,:]))