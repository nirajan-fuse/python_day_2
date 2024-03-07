# Implement a program that reads user input for a password. Create a custom exception WeakPasswordError to handle cases where 
# the password is shorter than 8 characters.

class WeakPasswordException(Exception):
    "Raised when password is shorter than 8 characters."
    pass

def password_validation():
    try:
        password = input("Enter a password: ")
        length = len(password)
        if length < 8:
            raise WeakPasswordException
        else:
            return 'Password is valid.'
    except WeakPasswordException:
        return 'WeakPasswordError: Password cannot be shorter than 8 characters!'
    
print(password_validation())
