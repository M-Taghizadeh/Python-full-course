"""
Author: Mohammad Taghizadeh
YouTube: https://www.youtube.com/c/MohammadTaghizadeh
"""


# python -m pip install mysql-connector

# Test connection:
import mysql.connector

# create connection:
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)
print(mydb)

