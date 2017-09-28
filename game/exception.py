def get_input():
    user_input = input("Enter something: ")
    if len(user_input) == 0:
        raise IOError("User entered nothing")
 
get_input()