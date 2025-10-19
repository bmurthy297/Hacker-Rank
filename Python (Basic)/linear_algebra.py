# Linear Algebra : https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy

N = int(input())

my_array = numpy.array([input().split() for _ in range(N)], float)

print(round(numpy.linalg.det(my_array),2))
