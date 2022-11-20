# Written by: Sumi
# Tested by:
# Debugged by:
# testing script to import .csv into mysql

import MySQLdb
import csv
import sys
conn = MySQLdb.connect(host="localhost", user="root", password="Autocrawler", database="carlistingsdb")

cursor = conn.cursor()
csv_data = csv.reader(open('cars/data/Autotrader_page1.csv'))
header = next(csv_data)

print('Importing the CSV Files')
for row in csv_data:
    print(row)
    cursor.execute(
        "INSERT INTO cars_car (name,price,mileage,dealer_name,carURL) VALUES (%s, %s, %s %s, %s)", row)

conn.commit()
cursor.close()