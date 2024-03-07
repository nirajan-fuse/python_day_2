# Implement a program that reads a CSV file named "data.csv," containing columns "Name" and "Age." Create a new CSV file 
# called "adults.csv" with only the rows of individuals who are 18 years or older.

import csv

with open('data.csv') as file:
    datas = csv.DictReader(file)

    with open('adult.csv', 'a') as sub_file:
        writer = csv.DictWriter(sub_file, fieldnames=['Name', 'Age'])

        for data in datas:
            if int(data['Age']) >= 18:
                writer.writerow({'Name': data['Name'], 'Age': data['Age']})