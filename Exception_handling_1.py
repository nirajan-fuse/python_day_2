# Write a Python program that takes two integers as input and performs division (num1 / num2). 
# Handle the ZeroDivisionError and display a custom error message when the second number is zero.

def division(num1: int, num2: int):
    try:
        result = num1 / num2
    except Exception as e:
        return "ZeroDivisionError: Cannot divide by zero."
    else:
        return result
   

print(division(45, 8))

print(division(4, 0))
