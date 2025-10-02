# Collections.OrderedDict() : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

n = int(input())
B = OrderedDict()
for _ in range(n):
    *item, price = input().split()
    name = ' '.join(item)
    price = int(price)
    B[name] = B.get(name, 0) + price

for name, total in B.items():
    print(name, total)



