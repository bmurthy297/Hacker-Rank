# Set .discard(), .remove() & .pop() : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

if __name__ == '__main__':
    n = int(input())  # Number of elements in the set
    s = set(map(int, input().split()))  # Initialize the set with input values
    N = int(input())  # Number of commands to execute
    for _ in range(N):
        command = input().split()  # Read each command
        if command[0] == 'pop':
            s.pop()  # Remove and return an arbitrary element from the set
        elif command[0] == 'remove':
            s.remove(int(command[1]))  # Remove the specified element; raises KeyError if not found
        elif command[0] == 'discard':
            s.discard(int(command[1]))  # Remove the specified element if present; does nothing if not found
    print(sum(s))  # Print the sum of remaining elements in the set