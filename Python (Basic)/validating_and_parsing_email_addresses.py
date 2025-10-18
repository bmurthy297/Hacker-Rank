# Validating and Parsing Email Addresses : https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re
import email.utils

# Number of inputs
N = int(input())

# Loop through each name–email pair
for _ in range(N):
    s = input().strip()
    
    # Parse the name and email address using email.utils
    name, email_addr = email.utils.parseaddr(s)
    
    # Validate the email format using regex
    # Rules:
    # - username: starts with a letter, followed by letters, digits, -, ., _
    # - domain: only letters
    # - extension: 1 to 3 letters
    if re.match(r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email_addr):
        print(s)

