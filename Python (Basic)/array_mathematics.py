# Array Mathematics : https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

print(a + b)
print(a - b)        
print(a * b)
print(a // b)
print(a % b)
print(a ** b)