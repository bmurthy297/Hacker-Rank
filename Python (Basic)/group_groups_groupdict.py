# Group(), Groups() & Groupdict() : https://www.hackerrank.com/challenges/re-group-groups/problem

import re
m = re.search(r'([a-zA-Z0-9])\1+', input())
if m:
    print(m.group(1))
else:
    print(-1)   
    