# Company Logo : https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter


if __name__ == '__main__':
    s = input()

data = Counter(s)

sorted_data = sorted(data.items(), key=lambda x: (-x[1], x[0]))

for k, v in sorted_data[:3]:
    print(f"{k} {v}")


# Alternative solution without using Counter

if __name__ == '__main__':
    s = input().strip()
    freq = {}
    for char in s:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    for char, count in sorted_freq[:3]:
        print(f"{char} {count}")