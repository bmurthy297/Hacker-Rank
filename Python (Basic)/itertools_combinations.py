# itertools.combinations() : https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations
s, k = input().split()

lst = []

for i in range(1, int(k)+1):
    result = combinations(sorted(s), i)
    for r in result:
        print("".join(r))