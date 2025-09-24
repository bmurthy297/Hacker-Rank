# Check subset : https://www.hackerrank.com/challenges/py-check-subset/problem

T = int(input())

for _ in range(T):

    A = int(input())

    A = set(map(int, input().split()))

    B = int(input())

    B = set(map(int, input().split()))

    result = A.issubset(B)

    print(result)