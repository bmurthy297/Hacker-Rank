# Text Wrap : https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap     

def wrap(string, max_width):
    return textwrap.fill(string, max_width)         
    # return '\n'.join(textwrap.wrap(string, max_width))   # Another way to do the same thing           


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)