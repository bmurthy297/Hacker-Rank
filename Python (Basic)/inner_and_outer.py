# Inner and Outer : https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy

A = numpy.array(input().split(), int)

B = numpy.array(input().split(), int)

print(numpy.inner(A, B))

print(numpy.outer(A, B))