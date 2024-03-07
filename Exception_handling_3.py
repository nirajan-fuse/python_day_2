# Write a Python program that takes a user input and converts it to an integer. Handle the ValueError and display a custom error 
# message when the input cannot be converted to an integer.

def convert_to_integer():
    try:
        user_input = int(input("Enter a number: "))
    except ValueError:
        return 'Error: Cannot convert to integer!'
    else: 
        return user_input
    
print(convert_to_integer())