#Question - https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

# Number of shoes in stock
X = int(input())

# List of shoe sizes in stock
shoe_sizes = list(map(int, input().split()))

# Count available shoe sizes
shoe_size_data = Counter(shoe_sizes)

# Number of customers
N = int(input())

total_earning = 0

for _ in range(N):
    size, price = map(int, input().split())
    # If the requested size is available, sell it
    if shoe_size_data[size] > 0:
        total_earning += price
        shoe_size_data[size] -= 1

print(total_earning)
