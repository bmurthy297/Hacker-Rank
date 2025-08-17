# Find the Runner-Up Score! : https://www.hackerrank.com/challenges/find-the-runner-up-score/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = set(arr)  # Use a set to get unique scores
    unique_scores.remove(max(unique_scores))  # Remove the highest score
    print(max(unique_scores))  # Print the second highest score