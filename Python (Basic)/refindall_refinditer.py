# Re.findall() & Re.finditer() : https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re

s = input()
pattern = r'(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})(?=[bcdfghjklmnpqrstvwxyz])'
matches = re.findall(pattern, s, re.IGNORECASE)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)