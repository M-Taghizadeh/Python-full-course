import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "py_university"
)
mycursor = mydb.cursor()

# delete from table
sql = "delete from student where student_id = 6"
# mycursor.execute(sql)
# mydb.commit()

# update on table:
sql = """
update student
set average = 17.63
where student_id = 3
"""

mycursor.execute(sql)
mydb.commit()