# Collections.namedtuple() : https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple  
n = int(input())
A = input().split()
B = namedtuple('B', A)
B = [B(*input().split()) for _ in range(n)]
print(sum(int(b.MARKS) for b in B) / n)

