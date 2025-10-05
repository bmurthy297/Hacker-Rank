# Map and Lambda Function : https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x**3  # complete the lambda function
def fibonacci(n):
    # return a list of fibonacci numbers
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    