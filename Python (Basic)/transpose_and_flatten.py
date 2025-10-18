# Transpose and Flatten : https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np
N, M = map(int, input().split())
array = np.array([input().split() for _ in range(N)], int)
print(array.T)
print(array.flatten())
