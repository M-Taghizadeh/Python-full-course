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

# ### [Create Tables for Univerity DB]
# # 1)create Faculty Table:
# sql = """
# create table Faculty(
#   Faculty_ID int not null,
# 	Faculty_name varchar(30),
# 	Faculty_Admin varchar(30),
# 	YearOfFundation char(4),
# 	Faculty_Address varchar(50),

# 	primary key(Faculty_ID)
# )
# """
# mycursor.execute(sql)
#######################################################################

# # 2)create Field table 
# sql = """
# create table Field(
#   Field_ID int,
# 	Field_Name varchar(30),
# 	Orientation varchar(30),
# 	Course varchar(30),
# 	Faculty_ID int,

# 	primary key(Field_ID),
# 	foreign key(Faculty_ID) references Faculty(Faculty_ID)
# )
# """
# mycursor.execute(sql)
#######################################################################

# # 3)create Student Table : 
# sql = """
# Create table Student(
#     Student_ID int not null AUTO_INCREMENT,
#     Student_Name varchar(30) not null,
#     Student_Family varchar(30) not null,
#     Field_ID int not null,
#     Entrance_Year char(4),
#     Address varchar(50),
#     Average float,

#     PRIMARY KEY(Student_ID),
#     FOREIGN KEY(Field_ID) REFERENCES Field(Field_ID)
# )
# """
# mycursor.execute(sql)
#######################################################################

# # 4)create Master table:
# sql = """
# create table Master(
#   Master_ID int AUTO_INCREMENT primary key,
# 	Master_Name varchar(30),
# 	Master_Family varchar(30),
# 	Degree varchar(20),
# 	Field varchar(30),
# 	Faculty_Member bit,
# 	Faculty_ID int references Faculty(Faculty_ID),
# 	Phone char(11),
# 	Address varchar(50)
# )
# """
# mycursor.execute(sql)


# Show all tables
sql = "SHOW TABLES"
mycursor.execute(sql)
for table in mycursor:
    print(table)