# Sum and Prod : https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy

N, M = map(int, input().split())

arr = numpy.array([input().split() for _ in range(N)], int)

add = numpy.sum(arr,  axis=0)

print(numpy.prod(add))