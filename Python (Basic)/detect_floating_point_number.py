# Detect Floating Point Number : https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

def detect_float(s):
    # Regex pattern for a floating-point number
    # It allows for an optional sign (+ or -),
    # followed by zero or more digits, a mandatory decimal point,
    # and one or more digits after the decimal point.
    # It also handles cases like ".5" or "-.7"
    pattern = r"^[+-]?\d*\.\d+$"
    return bool(re.fullmatch(pattern, s))

# Example usage:
T = int(input())
for _ in range(T):
    N = input()
    print(detect_float(N))