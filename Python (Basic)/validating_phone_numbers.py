# Validating phone numbers : https://www.hackerrank.com/challenges/validating-the-phone-number/problem
import re
N = int(input())
for _ in range(N):
    phone = input()
    if re.match(r'^[789]\d{9}$', phone):
        print("YES")
    else:
        print("NO")