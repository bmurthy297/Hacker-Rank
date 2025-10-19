# Merge the Tools! : https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        unique_chars = ""
        for ch in substring:
            if ch not in unique_chars:
                unique_chars += ch
        print(unique_chars)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)