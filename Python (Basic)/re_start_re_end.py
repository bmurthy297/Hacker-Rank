# Re.start() & Re.end() : https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

# Read the input strings
s = input()
k = input()

# Use a positive lookahead to find all occurrences, including overlapping ones
pattern = r'(?=' + re.escape(k) + r')'

# Find all matches using re.finditer
matches = re.finditer(pattern, s)

# Store the results in a list
results = []
for match in matches:
    # re.finditer with a lookahead returns a match object for the empty string
    # at the start of each match. The start() method gives the starting index.
    start_index = match.start()
    # The end index is calculated by adding the length of the substring k.
    # We subtract 1 because end() returns one past the last character.
    end_index = start_index + len(k) - 1
    results.append((start_index, end_index))

# Check if any matches were found and print the result
if results:
    for r in results:
        print(r)
else:
    print((-1, -1))

