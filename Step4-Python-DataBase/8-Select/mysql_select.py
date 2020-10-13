import mysql.connector

# Connection to my Database:
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "py_University"
)

# Create Cursor:
mycursor = mydb.cursor()

# SELECT FROM
print("----------------------------------------------\n[Faculty]\n")
sql = "select * from faculty"
mycursor.execute(sql)
myresult = mycursor.fetchall() ###fetchall() function for fetch all of record of table
for record in myresult:
    print(record)


print("----------------------------------------------\n[Field]")
sql = "select * from Field"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for record in myresult:
    print(record)


print("----------------------------------------------\n[Master]")
sql = "select * from Master"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for record in myresult:
    print(record)


print("----------------------------------------------\n[Student]")
sql = "select * from Student"
mycursor.execute(sql)
myresult = mycursor.fetchall() 
for record in myresult:
    print(record)