# Designer Door Mat: https://www.hackerrank.com/challenges/designer-door-mat/problem

def designer_door_mat(n, m):
    # Create the top half pattern using '.|.' motifs, centered with '-'
    pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
    # Join the top half, the 'WELCOME' line, and the mirrored bottom half
    return '\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1])  

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(designer_door_mat(n, m))
