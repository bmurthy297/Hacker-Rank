# difference : https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
s1 = set(map(int, input().split()))

b = int(input())
s2 = set(map(int, input().split()))

print(len(s1.difference(s2)))