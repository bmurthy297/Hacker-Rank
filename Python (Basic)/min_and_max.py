# Min and Max : https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy

N, M = map(int, input().split())

my_array = numpy.array([input().split() for _ in range(N)], int)

min_list = numpy.min(my_array, axis=1)

print(numpy.max(min_list))