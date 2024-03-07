# Write a Python program that takes two integers as input and performs division (num1 / num2). Handle both ValueError (if 
# non-integer input) and ZeroDivisionError and display appropriate error messages.

def division():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        return f"Error: Please enter integers only."
    except ZeroDivisionError:
        return f"Error: Division by zero is not allowed."
    else:
        return f"Result of division: {result}"
    
print(division())

