# String Formatting : https://www.hackerrank.com/challenges/python-string-formatting

def print_formatted(number):
    width = len(bin(number)) - 2  # Calculate the width needed for binary representation
    for i in range(1, number + 1):
        # Print the formatted string with right alignment
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")   

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)