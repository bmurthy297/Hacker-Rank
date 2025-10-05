# All or Any : https://www.hackerrank.com/challenges/any-or-all/problem

n = int(input())
numbers = list(map(int, input().split()))

# Condition 1: All numbers are positive
all_positive = all(num > 0 for num in numbers)

# Condition 2: Any number is a palindrome
any_palindrome = any(str(num) == str(num)[::-1] for num in numbers)

# Print True if both conditions are met, otherwise False
print(all_positive and any_palindrome)