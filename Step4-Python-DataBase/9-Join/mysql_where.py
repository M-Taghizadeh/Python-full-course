import mysql.connector

def read_from_table(sql):
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for record in myresult:
        print(record)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "py_university"
)
mycursor = mydb.cursor()

### [WHERE]
# 1:
sql = "select * from student where address = 'tehran'"
read_from_table(sql)

print("---------------------------------------------------------")
# 2:
sql = "select * from Master where faculty_member = 1"
read_from_table(sql)

print("---------------------------------------------------------")
# 3:
sql = "select * from Student where average<12"
read_from_table(sql) 

print("---------------------------------------------------------")
# 4:
sql = "select * from student where average>=17 order by average desc"
read_from_table(sql)

print("---------------------------------------------------------")
# 5:
sql = "select * from Master Where Degree = 'dr'"
read_from_table(sql)
print("---------------------------------------------------------")

### [JOIN]
# 6:
sql = "select * from student, field where student.field_id = field.field_id and orientation = 'software'"
read_from_table(sql)

print("---------------------------------------------------------")
# 7:
sql = "select * from field, faculty where faculty.faculty_ID = field.field_ID and faculty_name = 'Computer Faculty'"
read_from_table(sql)
print("---------------------------------------------------------")