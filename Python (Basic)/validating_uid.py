# Validating UID : https://www.hackerrank.com/challenges/validating-uid/problem

import re

N = int(input())

for _ in range(N):
    uid = input().strip()
    
    # Check length = 10
    if len(uid) != 10:
        print("Invalid")
        continue
    
    # Check all alphanumeric
    if not uid.isalnum():
        print("Invalid")
        continue
    
    # Check no repeating characters
    if len(set(uid)) != 10:
        print("Invalid")
        continue
    
    # Check at least 2 uppercase letters and 3 digits
    if len(re.findall(r'[A-Z]', uid)) < 2 or len(re.findall(r'\d', uid)) < 3:
        print("Invalid")
        continue
    
    print("Valid")
