"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


import mysql.connector

# Connect to server:
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = ""
)
# Create cursor for execute sql query
mycursor = mydb.cursor()

# Create Data Base: 
sql = "CREATE DATABASE py_University"
mycursor.execute(sql)

# show all databases:
sql = "SHOW DATABASES"
mycursor.execute(sql)

for database in mycursor:
    print (database)