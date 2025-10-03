# Incorrect Regex : https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

def is_valid_pattern(pattern):
    try:
        # Compile the pattern to check for validity
        re.compile(pattern)
    except re.error:
        return False
    
    # Detect patterns where quantifiers are used improperly
    if re.search(r'.*[\+\*]{2,}', pattern):
        return False

    return True

for _ in range(int(input())):
    pattern = input()
    if is_valid_pattern(pattern):
        print("True")
    else:
        print("False")


