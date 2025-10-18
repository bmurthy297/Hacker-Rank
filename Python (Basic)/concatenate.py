# Concatenate : https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np
N, M, P = map(int, input().split()) 
array1 = np.array([input().split() for _ in range(N)], int)
array2 = np.array([input().split() for _ in range(M)], int)
print(np.concatenate((array1, array2), axis=0)) 
