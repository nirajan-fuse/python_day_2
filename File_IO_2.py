# Create a function add_to_json that takes a filename and a new_data as input. The function should read the JSON data from 
# the file, add the new new_data to it, and write the updated data back to the same file.

# Sample Json: 
# [
#   {
#     "name": "Ram",
#     "age": 30
#   },
#   {
#     "name": "Sita",
#     "age": 25
#   }
# ]

import json

def add_to_json(filename: str, new_data: dict):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(filename, 'w') as new_file:
                data_list = [new_data]
                json.dump(data_list, new_file, indent=4)
                return 

        data.append(new_data)

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

new_data = {
     'Name': 'Shyam',
     'Age': 23
} 

add_to_json('data.json', new_data)
