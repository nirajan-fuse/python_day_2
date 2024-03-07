# Implement a program that takes user input for a filename, opens the file in read mode, and displays its contents. 
# Handle the FileNotFoundError and display an error message if the file is not found.

def display_file_content():
    try:
        filename = input("Enter the filename: ")
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('Error: File not found!')

display_file_content()