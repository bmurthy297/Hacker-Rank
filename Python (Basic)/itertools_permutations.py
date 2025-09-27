# itertools.permutations() : https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations      
s, k = input().split()
perms = permutations(sorted(s), int(k))

for p in perms:
    print(''.join(p))
    