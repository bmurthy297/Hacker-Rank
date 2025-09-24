# Set Mutation : https://www.hackerrank.com/challenges/py-set-mutations/problem

n = int(input())
s = set(map(int, input().split()))          

m = int(input())
for _ in range(m):
    cmd, num = input().split()
    nums = set(map(int, input().split()))
    if cmd == 'intersection_update':
        s.intersection_update(nums)
    elif cmd == 'update':
        s.update(nums)
    elif cmd == 'symmetric_difference_update':
        s.symmetric_difference_update(nums)
    elif cmd == 'difference_update':
        s.difference_update(nums)

print(sum(s))   
