# Exceptions : https://www.hackerrank.com/challenges/exceptions/problem

for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except (ValueError, ZeroDivisionError) as e:
        print("Error Code:", e) 

        