# Zipped : https://www.hackerrank.com/challenges/zipped/problem

n, x = map(int, input().split())  

marks = []  
for _ in range(x):
    marks.append(map(float, input().split()))


for student in zip(*marks):
    print(sum(student)/x)

