# itertools.combinations_with_replacement() : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement
s, k = input().split()
comb = combinations_with_replacement(sorted(s), int(k))
for c in comb:
    print(''.join(c))
    
