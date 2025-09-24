# Check Strict Superset : https://www.hackerrank.com/challenges/py-check-strict-superset/problem

n = int(input())  
s = set(map(int, input().split()))

m = int(input())
flag = True
for _ in range(m):
    s1 = set(map(int, input().split()))
    if not s.issuperset(s1) or len(s) == len(s1):
        flag = False
        break

print(flag) 
