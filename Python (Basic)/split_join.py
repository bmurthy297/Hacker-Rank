# Split and Join : https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # Split the string into a list of words
    words = line.split(" ")
    # Join the list of words with a hyphen
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)