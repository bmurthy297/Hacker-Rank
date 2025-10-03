# Input() : https://www.hackerrank.com/challenges/input/problem

x, k = map(int, input().split())

poly = input()

print(eval(poly) == k)