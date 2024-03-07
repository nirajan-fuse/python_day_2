# Write a Python program that takes user input for age. Create a custom exception InvalidAgeError to handle cases where the 
# age is below 0 or above 120.


class InvalidAgeException(Exception):
    "Raised when the input value is below 0 or above 120."
    pass

def age_validation():
    try:
        age = int(input('Enter the age:'))
        if not 0 < age <= 120:
            raise InvalidAgeException
        else:
            return 'Age is valid.'
    except InvalidAgeException:
        return 'InvalidAgeError: Age cannot be below 0 or above 120!'
    

print(age_validation())
    

