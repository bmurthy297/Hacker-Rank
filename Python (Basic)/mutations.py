# Mutations : https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    # Convert the string to a list to allow mutation
    string_list = list(string)
    
    # Replace the character at the specified position
    string_list[position] = character
    
    # Join the list back into a string and return it
    return ''.join(string_list)

# Example usage:
if __name__ == '__main__':
    s = input("Enter the original string: ")
    i, c = input("Enter position and character (space-separated): ").split()
    i = int(i)  # Convert position to an integer
    result = mutate_string(s, i, c)
    print(result)