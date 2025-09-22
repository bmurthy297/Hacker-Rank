# Alphabet Rangoli: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string 

def print_rangoli(size):
    alpha = string.ascii_lowercase  # All lowercase English letters
    L = []
    for i in range(size):
        # Create the pattern for the current row using letters from alpha[i] to alpha[size-1]
        s = "-".join(alpha[i:size])
        # Mirror the pattern and center it with '-'
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    # Combine the top half (reversed, excluding the first line) and the full list for symmetry
    print('\n'.join(L[:0:-1]+L))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)