# collections.deque() : https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque
N = int(input())
A = deque()
for _ in range(N):
    command = input().split()
    if command[0] == 'append':
        A.append(command[1])
    elif command[0] == 'appendleft':
        A.appendleft(command[1])
    elif command[0] == 'pop':
        A.pop()
    elif command[0] == 'popleft':
        A.popleft()

print(' '.join(A))
