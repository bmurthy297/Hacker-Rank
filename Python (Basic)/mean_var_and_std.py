# Mean, Var, and Std : https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy

N, M = map(int, input().split())

my_array = numpy.array([input().split() for _ in range(N)], int)

print(numpy.mean(my_array, axis=1))

print(numpy.var(my_array, axis=0))

print(round(numpy.std(my_array, axis=None), 11))
