# Shape and Reshape : https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy as np
arr = np.array(input().split(), int)
print(np.reshape(arr, (3, 3)))

# alternative solution
import numpy

n = list(map(int, input().split()))

change_array = numpy.array(n)

change_array.shape = (3, 3)

print(change_array)