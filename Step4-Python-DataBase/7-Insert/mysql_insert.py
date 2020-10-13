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

# Insert one value into Faculty:
sql = "INSERT INTO Faculty (Faculty_ID, Faculty_Name, Faculty_Admin, YearOfFundation, Faculty_Address) VALUES (%s, %s, %s, %s, %s)"
val = (1, "Computer Faculty", "Dr Karimi", "1378", "Tehran")
mycursor.execute(sql, val)
mydb.commit() # for any change on database

# Insert many value into Faculty:
sql = "INSERT INTO Faculty (Faculty_ID, Faculty_Name, Faculty_Admin, YearOfFundation, Faculty_Address) VALUES (%s, %s, %s, %s, %s)"
val = [
    (2, "Software Engineering Faculty", "Dr Karimi", "1378", "Tehran"),
    (3, "Art Faculty" , "Dr Mohammadi", "1381", "Mashhad"),
    (4, "Math Faculty", "Dr Alavi", "1390", "Tabriz"),
    (5, "Industrial Faculty", "Dr Rezaei", "1381", "Esfehan"),
    (6, "Computer Faculty", "Dr Ghasemi", "1370", "Tehran")
]
mycursor.executemany(sql, val)
mydb.commit()
