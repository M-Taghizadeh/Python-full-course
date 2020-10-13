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

