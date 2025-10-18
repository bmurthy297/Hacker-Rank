# Zeros and Ones : https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy

shape = tuple(map(int, input().split()))

zero = numpy.zeros(shape, int)

one = numpy.ones(shape, int)

print(zero)
print(one)
