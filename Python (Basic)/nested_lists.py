# Nested Lists : https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Sort by score, then by name
    students.sort(key=lambda x: (x[1], x[0]))
    
    # Find the second lowest score
    second_lowest_score = sorted(set(score for name, score in students))[1]
    
    # Print names of students with the second lowest score
    for name, score in students:
        if score == second_lowest_score:
            print(name)