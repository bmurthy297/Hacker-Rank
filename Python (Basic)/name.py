# whats your name : https://www.hackerrank.com/challenges/whats-your-name/problem

def print_full_name(first, last):
    """
    This function takes a first name and a last name, and prints a greeting message.
    
    :param first: First name of the person
    :param last: Last name of the person
    """
    print(f"Hello {first} {last}! You just delved into python.")

# Input reading
if __name__ == '__main__':  
    first_name = input()
    last_name = input()
    
    # Call the function with the provided names
    print_full_name(first_name, last_name)